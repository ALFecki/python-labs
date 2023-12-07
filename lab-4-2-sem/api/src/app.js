const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();

const userRoute = require('./routes/userRoute');
const categoryRoute = require('./routes/categoryRoute');
const toyRoute = require('./routes/toyRoute');
const supplierRoute = require('./routes/supplierRoute');
const authRoute = require('./routes/authRoute');

const app = express();


mongoose.connect(process.env.DATABASE_URL)
    .then(() => console.log('Connected to the database'))
    .catch(err => {
        console.error('Error connecting to the database:', err);
        process.exit(1);
    });
app.use(cors());
app.use(express.json());

app.use('/api/user', userRoute);
app.use('/api/category', categoryRoute);
app.use('/api/toy', toyRoute);
app.use('/api/supplier', supplierRoute);
app.use('/api/auth', authRoute);

const PORT = process.env.PORT;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
