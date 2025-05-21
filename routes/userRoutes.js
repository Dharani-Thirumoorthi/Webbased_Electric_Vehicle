const express = require('express');
const router = express.Router();
const User = require('../models/User');

// POST route to create a new user
router.post('/users', async (req, res) => {
    const newUser = new User(req.body);
    await newUser.save();
    res.json(newUser);
});

// GET route to fetch all users
router.get('/users', async (req, res) => {
    const users = await User.find();
    res.json(users);
});

module.exports = router;
