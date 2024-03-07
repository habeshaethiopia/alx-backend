var kue = require("kue"),
  push_notification_code = kue.createQueue();

const job = push_notification_code.create("push_notification_code", {
  phoneNumber: "4153518780",
  message: "This is the code to verify your account",
});
job.save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
  else console.log(`Notification job failed`);
});
job.on("complete", () => {
  console.log("Notification job completed");
});
