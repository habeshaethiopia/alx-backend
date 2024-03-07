import { createClient } from "redis";
const client = createClient();

client.on("error", function (error) {
  console.error("Redis client not connected to the server: ", error);
});
client.on("connect", function () {
  console.log("Redis client connected to the server");
});

client.subscribe("holberton school channel");

client.on("message", function (channel, message) {
  if (channel === "holberton school channel") {
    console.log(message);
  }
});

client.on("KILL_SERVER", function (message) {
  client.unsubscribe('holberton school channel');
  client.quit();
});
