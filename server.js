const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const app = express();

// Middleware
app.use(express.json());
app.use(cors());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/dharaniDB', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.log(err));

// Define a basic route
app.get('/', (req, res) => {
    res.send('Backend is running');
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
const userRoutes = require('./routes/userRoutes');
app.use('/api', userRoutes);


const prebookRoutes = require('./routes/prebookRoutes');
app.use('/api', prebookRoutes);
