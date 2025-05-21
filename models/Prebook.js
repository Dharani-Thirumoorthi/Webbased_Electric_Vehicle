const mongoose = require('mongoose');

const PrebookSchema = new mongoose.Schema({
    name: String,
    email: String,
    model: String,
});

module.exports = mongoose.model('Prebook', PrebookSchema);
