(function () {
  // Ink wash + splatter, painted behind elements marked data-ink (echoes the Squad cover art)
  function rng(seed) { return function () { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }; }
  function paintInk(el) {
    var c = el.querySelector("canvas.ink");
    if (!c) { c = document.createElement("canvas"); c.className = "ink"; c.setAttribute("aria-hidden", "true"); el.prepend(c); }
    var w = el.clientWidth, h = el.clientHeight, dpr = Math.min(window.devicePixelRatio || 1, 2);
    if (!w || !h) return;
    c.width = w * dpr; c.height = h * dpr;
    var x = c.getContext("2d"); x.scale(dpr, dpr); x.clearRect(0, 0, w, h);
    var r = rng(Number(el.getAttribute("data-ink-seed") || 7));
    var mode = el.getAttribute("data-ink");
    var dark = el.classList.contains("band-ink");
    var tones = dark ? ["255,255,255", "225,225,218", "190,192,180", "150,152,140", "120,122,112"] : ["17,17,17", "40,40,38", "70,72,66", "110,114,100", "150,152,140"];
    function blob(cx, cy, rad, a, tone) {
      var g = x.createRadialGradient(cx, cy, 0, cx, cy, rad);
      if (dark) a *= 0.55;
      g.addColorStop(0, "rgba(" + tone + "," + a + ")");
      g.addColorStop(0.6, "rgba(" + tone + "," + a * 0.45 + ")");
      g.addColorStop(1, "rgba(" + tone + ",0)");
      x.fillStyle = g; x.beginPath(); x.arc(cx, cy, rad, 0, Math.PI * 2); x.fill();
    }
    // Smoke band along the bottom
    var band = mode === "poster" ? 0.34 : 0.22;
    var n = Math.round(w / 6);
    for (var i = 0; i < n; i++) {
      var px = r() * w;
      var ridge = h * (1 - band) + Math.sin(px / w * Math.PI * 3 + 1.3) * h * 0.06 + r() * h * 0.08;
      var py = ridge + Math.pow(r(), 0.7) * (h - ridge + 40);
      blob(px, py, 18 + r() * (mode === "poster" ? 90 : 60), 0.05 + r() * 0.12, tones[Math.floor(r() * tones.length)]);
    }
    // Dark ink ridge line
    for (var j = 0; j < n / 2; j++) {
      var qx = r() * w;
      var qy = h * (1 - band) + Math.sin(qx / w * Math.PI * 3 + 1.3) * h * 0.06 + r() * 30 + 10;
      blob(qx, qy, 10 + r() * 30, 0.08 + r() * 0.14, tones[Math.floor(r() * 2)]);
    }
    // Splatter in the top corners
    if (mode === "poster") {
      for (var k = 0; k < 900; k++) {
        var side = r() < 0.5 ? 0 : 1;
        var sx = side ? w - Math.pow(r(), 1.8) * w * 0.45 : Math.pow(r(), 1.8) * w * 0.45;
        var sy = Math.pow(r(), 2.2) * h * 0.45;
        var dist = Math.hypot(side ? w - sx : sx, sy) / (w * 0.5);
        var sr = Math.max(0.4, (1 - dist) * 2.6 * r());
        x.fillStyle = "rgba(17,17,17," + (0.25 + r() * 0.6) + ")";
        x.beginPath(); x.arc(sx, sy, sr, 0, Math.PI * 2); x.fill();
      }
      for (var m = 0; m < 26; m++) {
        var side2 = r() < 0.5 ? 0 : 1;
        blob(side2 ? w - r() * w * 0.12 : r() * w * 0.12, r() * h * 0.12, 20 + r() * 50, 0.25 + r() * 0.35, tones[0]);
      }
    }
  }
  var inked = document.querySelectorAll("[data-ink]");
  inked.forEach(paintInk);
  var rt; window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(function () { inked.forEach(paintInk); }, 150); });

  // Next 2nd Friday of the month (Impossible Task Squad meetup)
  function secondFriday(year, month) {
    var d = new Date(year, month, 1);
    var offset = (5 - d.getDay() + 7) % 7; // first Friday
    return new Date(year, month, 1 + offset + 7);
  }
  function nextMeetup() {
    var now = new Date();
    var today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    var d = secondFriday(today.getFullYear(), today.getMonth());
    if (d < today) d = secondFriday(today.getFullYear(), today.getMonth() + 1);
    return d;
  }
  var m = nextMeetup();
  var months = ["January","February","March","April","May","June","July","August","September","October","November","December"];
  document.querySelectorAll("[data-meetup-day]").forEach(function (el) { el.textContent = m.getDate(); });
  document.querySelectorAll("[data-meetup-month]").forEach(function (el) { el.textContent = months[m.getMonth()] + " " + m.getFullYear(); });
  document.querySelectorAll("[data-meetup-mon]").forEach(function (el) { el.textContent = months[m.getMonth()].slice(0, 3); });
  document.querySelectorAll("[data-meetup-long]").forEach(function (el) { el.textContent = "Friday, " + months[m.getMonth()] + " " + m.getDate(); });

  // Friendly placeholder when an image file isn't available
  function swap(img) {
    if (img.dataset.swapped) return;
    img.dataset.swapped = "1";
    var box = document.createElement("div");
    box.className = "img-missing";
    box.textContent = img.alt ? "Image: " + img.alt : "Image coming soon";
    img.replaceWith(box);
  }
  document.querySelectorAll("img").forEach(function (img) {
    if (img.complete && img.naturalWidth === 0) swap(img);
    img.addEventListener("error", function () { swap(img); });
  });

  // Copy buttons
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy");
      var done = function () { var t = btn.textContent; btn.textContent = "Copied"; setTimeout(function () { btn.textContent = t; }, 1600); };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { selectNear(btn); });
      } else { selectNear(btn); }
    });
  });
  function selectNear(btn) {
    var code = btn.parentElement.querySelector("code");
    if (!code) return;
    var r = document.createRange(); r.selectNodeContents(code);
    var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
  }

  // Which Social Media Fits You? quiz
  var form = document.getElementById("quiz-form");
  if (form) {
    var data = JSON.parse(document.getElementById("quiz-platforms").textContent);
    var groups = form.querySelectorAll("fieldset.q");
    var total = groups.length;
    var progress = document.getElementById("quiz-progress");
    var result = document.getElementById("quiz-result");
    function answered() { return form.querySelectorAll("input:checked").length; }
    function update() { progress.textContent = answered() + " of " + total + " answered"; }
    form.addEventListener("change", update);
    update();
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (answered() < total) {
        var first = Array.prototype.find.call(groups, function (f) { return !f.querySelector("input:checked"); });
        progress.textContent = "Answer every question to see your match (" + (total - answered()) + " left).";
        if (first) { first.scrollIntoView({ behavior: "smooth", block: "center" }); var i = first.querySelector("input"); if (i) i.focus({ preventScroll: true }); }
        return;
      }
      var score = {};
      data.order.forEach(function (k) { score[k] = 0; });
      form.querySelectorAll("input:checked").forEach(function (inp) {
        var list = inp.value.split(" ");
        list.forEach(function (k, idx) { score[k] += idx === 0 ? 2 : 1; });
      });
      var ranked = data.order.slice().sort(function (a, b) { return score[b] - score[a] || data.order.indexOf(a) - data.order.indexOf(b); });
      var best = data.platforms[ranked[0]], second = data.platforms[ranked[1]];
      result.querySelector("[data-type]").textContent = best.name;
      result.querySelector("[data-why]").textContent = best.why;
      var ol = result.querySelector("[data-start]"); ol.innerHTML = "";
      best.start.forEach(function (t) { var li = document.createElement("li"); li.textContent = t; ol.appendChild(li); });
      result.querySelector("[data-time]").textContent = best.time;
      var g = result.querySelector("[data-guide]");
      if (best.guide) { g.hidden = false; g.innerHTML = ""; g.appendChild(document.createTextNode("Read our free guide: ")); var a = document.createElement("a"); a.href = best.guide[0]; a.textContent = best.guide[1]; g.appendChild(a); }
      else { g.hidden = true; }
      result.querySelector("[data-runner]").textContent = second.name + ".";
      result.querySelector("[data-runner-why]").textContent = second.why.split(". ")[0] + ".";
      result.hidden = false;
      result.scrollIntoView({ behavior: "smooth", block: "start" });
    });
    form.addEventListener("reset", function () { result.hidden = true; setTimeout(update, 0); window.scrollTo({ top: 0, behavior: "smooth" }); });
  }
})();

// Classes page: filter by learning path (#everyday / #business / #all)
(function () {
  var cats = document.querySelectorAll(".cat[data-paths]");
  if (!cats.length) return;
  var btns = document.querySelectorAll(".pf");
  function apply() {
    var h = (location.hash || "").slice(1);
    var f = (h === "everyday" || h === "business") ? h : "all";
    cats.forEach(function (c) { c.hidden = f !== "all" && c.getAttribute("data-paths").split(" ").indexOf(f) < 0; });
    btns.forEach(function (b) { b.setAttribute("aria-current", b.getAttribute("data-filter") === f ? "true" : "false"); });
    var target = document.getElementById(h);
    if (target && target.classList.contains("cat")) target.scrollIntoView({ block: "start" });
  }
  window.addEventListener("hashchange", apply);
  apply();
})();
