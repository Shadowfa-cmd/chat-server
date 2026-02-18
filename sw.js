self.addEventListener('install', event => {
  event.waitUntil(
    caches.open('shadow-chat-cache').then(cache => {
      return cache.addAll([
        '/',
        '/chat_secure.html'
      ]);
    })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => response || fetch(event.request))
  );
});
