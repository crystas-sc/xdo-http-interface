const staticDevCoffee = "cremote";
const assets = [
  "/",
  "/index.html",
  "/serviceWorker.js"
];

self.addEventListener("install", installEvent => {
  installEvent.waitUntil(
    caches.open(staticDevCoffee).then(cache => {
      cache.addAll(assets);
    })
  )
})
