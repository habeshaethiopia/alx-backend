import { createClient, print } from "redis";
import { promisify } from "util";
const client = createClient();

client.on("error", function (error) {
  console.error("Redis client not connected to the server: ", error);
});
client.on("connect", function () {
  console.log("Redis client connected to the server");
});
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}


async function displaySchoolValue(schoolName) {
  await client.get(schoolName, (error, value) => {
    console.log(value);
  });
}
displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
const hash = {
  HolbertonSchools: {
    Portland: "50",
    Seattle: "80",
    "New York": "60",
    Bogota: "20",
    Cali: "40",
    Paris: "2",
  },
};
for (const school in hash.HolbertonSchools) {
  client.hset("HolbertonSchools", school, hash.HolbertonSchools[school], print);
}
client.hgetall("HolbertonSchools", function (error, object) {
  console.log(object);
});