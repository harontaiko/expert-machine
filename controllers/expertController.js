const path = require('path');

const { spawn } = require('child_process');

const askExpert = async (req, res) => {
    const { prompt } = req.body;

    // Get absolute path to recommendation.py script
    const scriptPath = path.join(__dirname, '..', 'python', 'recommendation.py');

    // Get absolute path to python executable
    const pythonPath = '/usr/bin/python3';

    // Spawn child process for recommendation.py script
    const pythonProcess = spawn(pythonPath, [scriptPath, prompt]);

    let recommendation = '';

    // output
    pythonProcess.stdout.on('data', (data) => {
        recommendation += data.toString();
    });

    // Err listener
    pythonProcess.stderr.on('data', (data) => {
        console.error(`Error: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        if (code === 0) {
            res.status(200).json({
                success: true,
                recommendation: recommendation.trim(),
            });
        } else {
            console.error(`Python script exited with code ${code}`);
            res.status(500).json({
                success: false,
                error: `Python script exited with code ${code}`,
            });
        }
    });
};

module.exports = { askExpert };
