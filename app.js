//require express server body parser ans environment var
const path = require('path');
const express = require('express');
const dotenv = require('dotenv').config();
const port = process.env.PORT || 3000;

const app = express();

app.use(express.json());

app.use(express.urlencoded({extended:false}));

//views
app.use(express.static(path.join(__dirname, 'public')));

app.use('/expert', require('./routes/ExpertRoute'));

app.listen(port, () => console.log(`Server running on port ${port}`));