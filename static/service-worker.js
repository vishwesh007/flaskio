// static/service-worker.js
self.addEventListener('push', event => {
    const options = {
        body: event.data.text(),
    };

    event.waitUntil(
        self.registration.showNotification('Push Notification', options)
    );
});
