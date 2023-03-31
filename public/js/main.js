function onSubmit(e) {
    e.preventDefault();
  
    //clear current recs
    document.querySelector('#output').textContent = '';
    document.querySelector('.time-out').innerHTML = '';
  
    const prompt = document.querySelector('#prompt').value;
  
    if (prompt === '') {
      alert('input is missing, please provide question to continue');
      return;
    }
  
    askExpert(prompt);
  }
  
  async function askExpert(prompt) {
    try {
      showSpinner();

      const startTime = performance.now(); 
  
      const response = await fetch('/expert/ask', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          prompt,
        }),
      });

      const endTime = performance.now(); 
  
      if (!response.ok) {
        removeSpinner();
        throw new Error('Engine Error occurred, please try again');
      }
  
      const data = await response.json();
      console.log(data);
      

      let recOutput = document.querySelector('#output');

      recOutput.classList.add('shown');

      const clearTime = Math.round(((endTime - startTime)/1000) * 10) / 10; 

      document.querySelector('.time-out').innerHTML = `${clearTime}s`
      //log rec
      result = `${data.recommendation}`;
      let i = 0;
      const interval = setInterval(() => {
        recOutput.textContent += result.charAt(i);
        i++;
        if(i > result.length){
          clearInterval(interval);
        }
      }, 40);
  
      removeSpinner();
    } catch (error) {
      document.querySelector('#output').classList.add('shown');
      document.querySelector('#output').textContent = error;
    }
  }
  
  function showSpinner() {
    document.querySelector('.spinner-container').classList.add('shown');
  }
  
  function removeSpinner() {
    document.querySelector('.spinner-container').classList.remove('shown');
  }
  
  document.querySelector('#expert-form').addEventListener('submit', onSubmit);