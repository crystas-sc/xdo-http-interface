const staticDevCoffee = "cremote";
const assets = [
  "/",
  "/index.html",
  "/assets/serviceWorker.js",
  "/assets/tailwind-1.9.6.css",
];

self.addEventListener("install", installEvent => {
  installEvent.waitUntil(
    caches.open(staticDevCoffee).then(cache => {
      cache.addAll(assets);
    })
  )
})
