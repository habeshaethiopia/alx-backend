import { createClient, print } from "redis";
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
function displaySchoolValue(schoolName) {
    client.get(schoolName, function (error, value) {
        console.log(value);
    });
    
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');