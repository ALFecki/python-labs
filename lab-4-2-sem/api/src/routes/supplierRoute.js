const express = require('express');
const router = express.Router();
const supplierController = require('../controllers/supplierController');
const authMiddleware = require('../middleware/middleware')

router.get('/', supplierController.getAll);
router.get('/:id', supplierController.getById);
router.post('/', authMiddleware, supplierController.create);
router.put('/:id', authMiddleware, supplierController.update);
router.delete('/:id', authMiddleware, supplierController.delete);

module.exports = router;
