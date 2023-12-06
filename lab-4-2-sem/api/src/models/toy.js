const mongoose = require('mongoose');

const toySchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, 'Toy name is required'],
        unique: true,
        trim: true,
        minlength: [3, 'Toy name must be at least 3 characters long'],
        maxlength: [50, 'Toy name cannot exceed 50 characters'],
    },
    description: {
        type: String,
        default: '',
        maxlength: [500, 'Toy description cannot exceed 500 characters'],
    },
    cost: {
        type: Number,
        required: [true, 'Toy cost is required'],
        min: [0, 'Toy cost cannot be negative'],
    },
    category: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Category',
        required: [true, 'Category is required for the toy'],
        validate: {
            validator: async function (value) {
                const category = await mongoose.model('Category').findById(value);
                return category !== null;
            },
            message: 'Invalid toy reference',
        },
    },
    supplier: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Supplier',
        required: [true, 'Supplier is required for the toy'],
        validate: {
            validator: async function (value) {
                const supplier = await mongoose.model('Supplier').findById(value);
                return supplier !== null;
            },
            message: 'Invalid supplier reference',
        },
    },
});

module.exports = mongoose.model('Toy', toySchema);
