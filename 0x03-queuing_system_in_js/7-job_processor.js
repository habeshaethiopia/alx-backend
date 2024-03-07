const blaclist = ["4153518780", "4153518781"];
function sendNotification(phoneNumber, message, job, done) {
  if (blaclist.includes(phoneNumber)) {
    return done(Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  job.progress(0, 100);
  job.progress(50, 100);
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
  done();
}
const kue = require("kue");
const queue = kue.createQueue();
queue.process("push_notification_code_2", (job, done) => {
  console.log(`Notification job ${job.id} created`);
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
