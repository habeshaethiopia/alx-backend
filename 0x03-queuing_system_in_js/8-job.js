function createPushNotificationsJobs(jobs, queue) {
    if (typeof (jobs) === 'object' && jobs.length > 0 )
    {
        for (const job of jobs) {
            const job_2 = queue.create('push_notification_code_3', job);
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
   }
    else {
         throw new Error('Jobs is not an array');
    }
}
module.exports = createPushNotificationsJobs;