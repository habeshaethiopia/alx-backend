const redis = require("redis");
const client = redis.createClient();
const { promisify } = require("util");
const listProducts = [
  { Id: 1, name: "Suitcase 250", price: 50, stock: 4 },
  { Id: 2, name: "Suitcase 450", price: 100, stock: 10 },
  { Id: 3, name: "Suitcase 650", price: 350, stock: 2 },
  { Id: 4, name: "Suitcase 1050", price: 550, stock: 5 },
];
function getItemsById(id) {
  return listProducts.filter((item) => item.Id === id);
}
const express = require("express");
const app = express();
app.listen(1245);
app.get("/list_products", (req, res) => {
  res.json(listProducts);
});

function reserveStockById(itemId, stock) {
  const item = getItemsById(itemId);
  client.hGet(itemId, (error, value) => {
    if (value < stock) {
      console.log(`Not enough stock available`);
    } else {
      client.hSet(itemId, value - stock, redis.print);
    }
  });
}
async function getCurrentReservedStockById(itemId) {
  return await client.hGet(itemId);
}
app.get("/list_products/:itemId", (req, res) => {
  if (res.getItemsById(req.params.itemId)) {
    res.json(getItemsById(req.params.itemId));
  } else {
    res.json({ status: "Product not found" });
  }
});
app.get("/reserve_product/:itemId/:stock", (req, res) => {
  if (getItemsById(req.params.itemId)) {
    if (getCurrentReservedStockById(req.params.itemId) < req.params.stock) {
      res.json({
        status: "Not enough stock available",
        itemId: req.params.itemId,
      });
    }
    reserveStockById(req.params.itemId, req.params.stock);
    res.json({ status: "Reservation confirmed", itemId: req.params.itemId });
  } else {
    res.json({ status: "Product not found" });
  }
});
