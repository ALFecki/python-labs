function Toy(name, price) {
    this.name = name;
    this.price = price;
}

Toy.prototype.getName = function () {
    return this.name;
}

Toy.prototype.getPrice = function () {
    return this.price;
}

function PlushToy(name, price, material) {
    Toy.call(this, name, price);
    this.material = material;
}

PlushToy.prototype = Object.create(Toy.prototype);
PlushToy.prototype.constructor = PlushToy;

PlushToy.prototype.getMaterial = function () {
    return this.material;
}

function withDiscount(prototype, method, discount) {
    const originalMethod = prototype[method];
    prototype[method] = function () {
        const price = originalMethod.call(this);
        return price - discount;
    }
}

const teddyBear = new PlushToy("Teddy Bear", 20, "Plush");
console.log(teddyBear.getName());
console.log(teddyBear.getPrice());
console.log(teddyBear.getMaterial());

withDiscount(PlushToy.prototype, "getPrice", 5);
console.log(teddyBear.getPrice());
