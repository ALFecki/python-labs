const mongoose = require('mongoose');

const supplierSchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, 'Supplier name is required'],
        unique: true,
        trim: true,
        minlength: [3, 'Supplier name must be at least 3 characters long'],
        maxlength: [50, 'Supplier name cannot exceed 50 characters'],
    },
    description: {
        type: String,
        default: '',
        maxlength: [500, 'Supplier description cannot exceed 500 characters'],
    },
});

module.exports = mongoose.model('Supplier', supplierSchema);
