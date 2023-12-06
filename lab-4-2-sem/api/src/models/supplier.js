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
    toy: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Toy',
        required: [true, 'Toy is required for the supplier'],
        validate: {
            validator: async function (value) {
                const toy = await mongoose.model('Toy').findById(value);
                return toy !== null;
            },
            message: 'Invalid toy reference',
        },
    },
});

module.exports = mongoose.model('Supplier', supplierSchema);
