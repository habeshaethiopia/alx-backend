const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
];
  
const kue = require('kue');
const push_notification_code_2 = kue.createQueue();
for (const job of jobs) {
    const job_2 = push_notification_code_2.create('push_notification_code_2', job);
    job_2.save((err) => {
        if (!err) console.log(`Notification job created: ${job_2.id}`);
    });
    job_2.on('complete', () => {
        console.log(`Notification job ${job_2.id} completed`);
    });
    job_2.on('failed', (error) => {
        console.log(`Notification job ${job_2.id} failed: ${error}`);
    });
    job_2.on('progress', (progress) => {
        console.log(`Notification job ${job_2.id} ${progress}% complete`);
    });
}