const express = require('express');
const router = express.Router();
const toyController = require('../controllers/toyController');
const authMiddleware = require('../middleware/authMiddleware')

router.get('/', toyController.getAll);
router.get('/:id', toyController.getById);
router.post('/', authMiddleware, toyController.create);
router.put('/:id', authMiddleware, toyController.update);
router.delete('/:id', authMiddleware, toyController.delete);

module.exports = router;
