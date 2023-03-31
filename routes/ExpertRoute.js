const express = require('express');
const {askExpert} = require('../controllers/expertController');
const router = express.Router();

router.post('/ask', askExpert);

module.exports = router;