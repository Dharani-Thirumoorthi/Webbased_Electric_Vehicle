const express = require('express');
const router = express.Router();
const Prebook = require('../models/Prebook');

// POST route to handle pre-booking submissions
router.post('/prebook', async (req, res) => {
    try {
        const newPrebook = new Prebook(req.body);
        await newPrebook.save();
        res.status(201).json({ message: 'Pre-booking successful' });
    } catch (error) {
        res.status(400).json({ message: 'Failed to submit pre-booking' });
    }
});

module.exports = router;
