<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <link rel="manifest" href="/assets/manifest.json" />

    <link href="/assets/tailwind-1.9.6.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.0/css/all.min.css" integrity="sha512-10/jx2EXwxxWqCLX/hHth/vu2KY3jCF70dCQB8TSgNjbCVAC/8vai53GfMDrO2Emgwccf2pJqxct9ehpzG+MTw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <style>
      .op-buttons, .top-items{
        display: flex;
        flex-wrap: wrap;
        width: 100%;
        
      }
      .op-buttons button{
        width: 12rem;
        /* font-size: 2em; */
        
      }
      .top-items button{
        /* font-size: 2em; */
      }
      .top-items input{
        width: 100%;
        /* font-size: 2em; */
      }
      :root{
         font-size : clamp(1rem, 2vw, 2rem);
      }
    </style>
  </head>

<body>
  <div class="hidden bg-red-600 shadow-lg mx-auto w-96 max-w-full text-sm pointer-events-auto bg-clip-padding rounded-lg block mb-3" id="alert" role="alert" aria-live="assertive" aria-atomic="true" data-mdb-autohide="false">
    
    <div class="p-3 bg-red-600 rounded-b-lg break-words text-white">
      WebSocket not connected
    </div>
  </div>
  <form id="form" method="get" onsubmit="return populateTimestamp()">
    <p class="form-label inline-block mb-2 text-gray-700 text-xl">Last command: <span  id="last-command">%(cmd)s %(key)s</span></p>
    <div class="top-items">
      <input type="text" name="cmd" value="%(cmd)s" class="form-control
      block
      w-full
      px-4
      py-2
      text-xl
      font-normal
      text-gray-700
      bg-white bg-clip-padding
      border border-solid border-gray-300
      rounded
      transition
      ease-in-out
      m-0
      focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" />
      
      <input type="text" name="key" value="%(key)s" class="form-control mt-6
      block
      w-full
      px-4
      py-2
      text-xl
      font-normal
      text-gray-700
      bg-white bg-clip-padding
      border border-solid border-gray-300
      rounded
      transition
      ease-in-out
      m-0
      focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" />
      <input type="hidden" name="timestamp" value="" />
      <button type="submit" class="inline-block px-6 py-2.5 bg-indigo-500  text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out" >submit</button>


      <button type="button" class="inline-block px-6 py-2.5 bg-indigo-500  text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out" onclick="sendClipboardData()">Send clipboard data</button>

    </div>

    
    <br />
    <div class="op-buttons flex justify-around " >
      

      <button type="button" class="bg-yellow-800 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded shadow-xl active:shadow-lg" onClick="btnClickKey('alt+Tab')">alt+Tab</button>
      <button type="button" class="bg-yellow-800 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded shadow-xl active:shadow-lg" onClick="btnClickKey('ctrl+F4')">ctrl+F4</button>

      <button type="button" class="bg-yellow-800 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded shadow-xl active:shadow-lg"  onClick="btnClickKey('alt+F4')">alt+F4</button>
      <button type="button" class="bg-yellow-800 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded shadow-xl active:shadow-lg"  onClick="btnClickMouse(' 0 0 click 1')">
        Left Click
      </button>
      <button type="button" class="bg-yellow-800 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded shadow-xl active:shadow-lg"  onClick="btnClickMouse(' 0 0 click 3')">
        Right Click
      </button>
      <!--
      <button type="button" class="bg-yellow-800 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded"  onmousedown="starttimer(event,' 0 0 click 4')" onmouseleave="stoptimer()" onmouseup="stoptimer()"  ontouchstart="starttimer(event,' 0 0 click 4')" ontouchend="stoptimer()" onClick1="btnClickMouse(' 0 0 click 4')">
        Scroll up
      </button>
      <button type="button"  class="bg-yellow-800 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded"  onmousedown="starttimer(event,' 0 0 click 5')" onmouseleave="stoptimer()" onmouseup="stoptimer()"  ontouchstart="starttimer(event,' 0 0 click 5')" ontouchend="stoptimer()" onClick1="btnClickMouse(' 0 0 click 5')">
        Scroll down
      </button>
      
      <button type="button"  class="bg-yellow-800 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded"  onClick="btnClickSetCmd('mousemove_relative --sync ')">
        Mouse Move
      </button>
      -->
      <button type="button" class="bg-yellow-800 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded shadow-xl active:shadow-lg"  onClick="btnClickSetCmd('key')">key cmd</button>
      <button type="button" class="bg-yellow-800 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded shadow-xl active:shadow-lg"  onClick="btnClickSetCmd('type')">type cmd</button>


      <button type="button" class="bg-yellow-800 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded shadow-xl active:shadow-lg"  onClick="btnClickKey('--clearmodifiers XF86AudioMute')">
        Mute
      </button>
      <!-- <button type="button" onClick="btnClickKey('--clearmodifiers XF86AudioPlay')">
        Play
      </button>
      <button type="button" onClick="btnClickKey('--clearmodifiers XF86AudioStop')">
        Stop
      </button>
      <button type="button" onClick="btnClickKey('--clearmodifiers XF86AudioPrev')">
        Prev
      </button>
      <button type="button" onClick="btnClickKey('--clearmodifiers XF86AudioNext')">
        Next
      </button>
      <button type="button" onmousedown="starttimer(event,'--clearmodifiers XF86AudioRaiseVolume', btnClickKey)" onmouseleave="stoptimer()" onmouseup="stoptimer()"  ontouchstart="starttimer(event,'--clearmodifiers XF86AudioRaiseVolume', btnClickKey)" ontouchend="stoptimer()" onClick1="btnClickKey('--clearmodifiers XF86AudioRaiseVolume')">
        Vol+
      </button>
      <button type="button" onmousedown="starttimer(event,'--clearmodifiers XF86AudioLowerVolume', btnClickKey)" onmouseleave="stoptimer()" onmouseup="stoptimer()"  ontouchstart="starttimer(event,'--clearmodifiers XF86AudioLowerVolume', btnClickKey)" ontouchend="stoptimer()" onClick1="btnClickKey('--clearmodifiers XF86AudioLowerVolume')">
        Vol-
      </button> -->
      <button class="bg-yellow-800 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded shadow-xl active:shadow-lg" type="button" onClick="btnClickKey('Return')">
        enter
      </button>

     
        
      
    </div>
    <div class="flex justify-around ">
      
      
        
        <button type="button" class="w-24 h-24 rounded-full bg-blue-500 focus:outline-none shadow-xl active:shadow-lg" onClick="btnClickKey('--clearmodifiers XF86AudioPlay')">
          <i class="fa fa-play fa-2x text-white"></i>
        </button> 
        <button type="button"  class="w-24 h-24 rounded-full bg-blue-500 focus:outline-none shadow-xl active:shadow-lg" onClick="btnClickKey('--clearmodifiers XF86AudioStop')">
          <i class="fa fa-stop fa-2x text-white"></i>
        </button> 
        <button type="button"  class="w-24 h-24 rounded-full bg-blue-500 focus:outline-none shadow-xl active:shadow-lg" onClick="btnClickKey('--clearmodifiers XF86AudioPrev')">
          <i class="fa fa-backward-step fa-2x text-white"></i>
        </button> 
        <button type="button"  class="w-24 h-24 rounded-full bg-blue-500 focus:outline-none shadow-xl active:shadow-lg" onClick="btnClickKey('--clearmodifiers XF86AudioNext')">
          <i class="fa fa-forward-step fa-2x text-white"></i>
        </button>
      
    </div>

    <br/>
    <track-pad></track-pad>
    <br/>
    <div class="flex justify-around ">
      
      
        <button class="bg-teal-800 focus:outline-none text-white text-3xl p-3 px-8 shadow-xl active:shadow-lg"
          onmousedown="starttimer(event,' 0 0 click 4')" onmouseleave="stoptimer()" onmouseup="stoptimer()"  ontouchstart="starttimer(event,' 0 0 click 4')" ontouchend="stoptimer()"
          >
          Scroll <i class="fa fa-arrow-up-long fa-1x text-white"></i>
        </button> 
        <button class="bg-blue-800 focus:outline-none text-white text-3xl p-3 px-8 w-1/6 rounded-full shadow-xl active:shadow-lg" 
          onmousedown="starttimer(event,'--clearmodifiers XF86AudioRaiseVolume', btnClickKey)" onmouseleave="stoptimer()" onmouseup="stoptimer()"  ontouchstart="starttimer(event,'--clearmodifiers XF86AudioRaiseVolume', btnClickKey)" ontouchend="stoptimer()" >
         <i class="fa fa-volume-high fa-1x text-white"></i>
        </button>
    </div>
    <div class="flex justify-around ">
      
      
      <button class="bg-teal-800 focus:outline-none text-white text-3xl p-3 px-8 shadow-xl active:shadow-lg"
        onmousedown="starttimer(event,' 0 0 click 5')" onmouseleave="stoptimer()" onmouseup="stoptimer()"  ontouchstart="starttimer(event,' 0 0 click 5')" ontouchend="stoptimer()"
        >Scroll 
        <i class="fa fa-arrow-down-long fa-1x text-white"></i>
      </button> 
      <button class="bg-blue-800 focus:outline-none text-white text-3xl p-3 px-8 w-1/6 rounded-full shadow-xl active:shadow-lg"
        onmousedown="starttimer(event,'--clearmodifiers XF86AudioLowerVolume', btnClickKey)" onmouseleave="stoptimer()" onmouseup="stoptimer()"  ontouchstart="starttimer(event,'--clearmodifiers XF86AudioLowerVolume', btnClickKey)" ontouchend="stoptimer()" > 
        <i class="fa fa-volume-low fa-1x text-white"></i>
      </button>
  </div>
    
    
    <br />
    <div style="display:grid; grid-template-columns:auto auto auto">
      <button style="grid-column:1/2" class=" h-24 bg-yellow-800 hover:bg-yellow-700 text-white font-bold py-4 px-4 rounded shadow-xl active:shadow-lg" type="button" onClick="btnClickKey('Escape')">
        Escape
      </button>
      <button style="grid-column:2/3" class="h-24 bg-blue-800 hover:bg-blue-700 text-white font-bold py-4 px-4 rounded shadow-xl active:shadow-lg" type="button" 
      onmousedown="starttimer(event,'Up', btnClickKey)" onmouseleave="stoptimer()" onmouseup="stoptimer()"  ontouchstart="starttimer(event,'Up', btnClickKey)" ontouchend="stoptimer()"  

      >
        up
      </button>
      <button style="grid-column:3/4" class=" h-24 bg-yellow-800 hover:bg-yellow-700 text-white font-bold py-4 px-4 rounded shadow-xl active:shadow-lg" type="button" onClick="btnClickKey('KP_Space')">
        Space
      </button>
      <button style="grid-column:1/2"  class="h-24 bg-blue-800 hover:bg-blue-700 text-white font-bold py-4 px-4 rounded shadow-xl active:shadow-lg" type="button" 
      onmousedown="starttimer(event,'Left', btnClickKey)" onmouseleave="stoptimer()" onmouseup="stoptimer()"  ontouchstart="starttimer(event,'Left', btnClickKey)" ontouchend="stoptimer()"  

      >
        left
      </button>
       
      <button style="grid-column:2/3"  class="h-24 bg-blue-800 hover:bg-blue-700 text-white font-bold py-4 px-4 rounded shadow-xl active:shadow-lg" type="button" onClick="btnClickKey('Return')">
        enter
      </button>
      <button  style="grid-column:3/4"  class="h-24 bg-blue-800 hover:bg-blue-700 text-white font-bold py-4 px-4 rounded shadow-xl active:shadow-lg" type="button" 
      onmousedown="starttimer(event,'Right', btnClickKey)" onmouseleave="stoptimer()" onmouseup="stoptimer()"  ontouchstart="starttimer(event,'Right', btnClickKey)" ontouchend="stoptimer()"  
            >
        right
      </button>
      <button style="grid-column:2/3"  class="h-24 bg-blue-800 hover:bg-blue-700 text-white font-bold py-4 px-4 rounded shadow-xl active:shadow-lg" type="button" 
      onmousedown="starttimer(event,'Down', btnClickKey)" onmouseleave="stoptimer()" onmouseup="stoptimer()"  ontouchstart="starttimer(event,'Down', btnClickKey)" ontouchend="stoptimer()"  

      >
        down
      </button>
    </div>
  </form>
  <a href="/fileserve" target="_blank">Static files</a>
  <form target="_blank" enctype = "multipart/form-data" action = "/fileupload" method = "post">
    <p>Upload File: <input type = "file" name = "file" /></p>
    <p><input type = "submit" value = "Upload" /></p>
  </form>

  


  <script>
    let timerId;
    let afterNumberOfTimers = 10;
    let counter=0;
    function starttimer(e,cmd, fn=btnClickMouse){
      if(e){
        e.preventDefault()
      }
      
      if(counter == 0){
        console.log("run cmd",cmd)
        fn(cmd)
      }
      counter++; 
      if(counter == afterNumberOfTimers){
        counter = 0;
      }
      
      timerId = requestAnimationFrame(()=>{starttimer(null,cmd, fn)})
    }
    function stoptimer(){
      cancelAnimationFrame(timerId)
    }
  </script>

    <script>
      var form = document.getElementById("form");

      function populateTimestamp() {
        if(window.websoc){
          window.websoc.send(`${form.cmd.value} ${form.key.value}`)
          return false;
        }
        form.timestamp.value =
          new Date().getTime() - new Date().getTimezoneOffset() * 60 * 1000;
        console.log("form.timestamp.value", form.timestamp.value);
        return true;
      }

      function btnClickKey(value) {
        if(window.websoc){
          window.websoc.send(`key ${value}`)
          return; 
        }
        form.cmd.value = "key";
        form.key.value = value;
        
        populateTimestamp();
        form.submit();
      }

      function btnClickMouse(value) {
        if(window.websoc){
          console.log("value",value)
          window.websoc.send(`mousemove_relative --sync ${value}`)
          return;
        }

        form.cmd.value = "mousemove_relative --sync ";
        form.key.value = value;
        
        populateTimestamp();
        form.submit();
      }

      function btnClickSetCmd(cmd) {
        form.cmd.value = cmd;
        form.key.value = "";
        form.key.focus();
      }
    </script>
    <style>
      button {
        min-height: 70px;
        min-width: 100px;
        margin: 10px;
      }
    </style>

    <script>
      function createFromData(cmd, key) {
        populateTimestamp();
        form.cmd.value = cmd;
        form.key.value = key;
        document.getElementById("last-command").innerHTML= `${cmd? cmd:""} ${key? key:""}`;
        var formData = new FormData(form);
        //formData.append("cmd", cmd);
        //formData.append("key", key);
        return formData;
      }

      function sendFormData(formData) {
        const data = [...formData.entries()];
        const asString = data
          .map(
            (x) => `${encodeURIComponent(x[0])}=${encodeURIComponent(x[1])}`
          )
          .join("&");
        console.log(asString);
        fetch("/?" + asString, {
          method: "GET",
        });
      }

      var trackPadElement = document.getElementsByTagName("track-pad")[0];
      trackPadElement.deltaCallBack = (delta) => {
        console.log("delta", delta);
        var xValue = delta.x < 0 ? "-- " + delta.x : delta.x;
        xValue = delta.x;
        if(window.websoc){
          window.websoc.send(`mousemove_relative --sync ${xValue} ${delta.y}`)
          return;
        }
        sendFormData(
          createFromData("mousemove_relative --sync ", `${xValue} ${delta.y}`)
        );
      };
      trackPadElement.leftClickCallBack = (touchPoint) => {
        console.log("left click - touchPoint", touchPoint);
        if(window.websoc){
          window.websoc.send(`mousemove_relative --sync 0 0 click 1`)
          return;
        }
        sendFormData(
          createFromData("mousemove_relative --sync ", ` 0 0 click 1`)
        );
      };

      trackPadElement.rightClickCallBack = (touchPoint) => {
        console.log("right click - touchPoint", touchPoint);
        if(window.websoc){
          window.websoc.send(`mousemove_relative --sync 0 0 click 3`)
          return;
        }
        sendFormData(
          createFromData("mousemove_relative --sync ", ` 0 0 click 3`)
        );
      };
      class Trackpad extends HTMLElement {
        constructor() {
          super();
        }

        connectedCallback() {
          this.render();
        }

        render() {
          const div = document.createElement("div");
          div.style.width = "100%";
          div.style.height = "500px";
          div.style.backgroundColor = "beige";
          div.ontouchmove = this.handleTouchMove;
          div.ontouchstart = this.handleTouchStart;
          div.ontouchend = this.handleTouchEnd;
          this.appendChild(div);

          //this.innerHTML = `<h1>Hello, World!</h1>`;
        }
        start = {
          x: 0,
          y: 0,
        };
        move = {
          x: 0,
          y: 0,
        };
        handleTouchStart = (event) => {
          event.preventDefault();
          this.start.x = event.touches[0].pageX;
          this.start.y = event.touches[0].pageY;
          this.move = {
            x: 0,
            y: 0,
          };
        };

        handleTouchEnd = (event) => {
          event.preventDefault();
          this.move = {
            x: 0,
            y: 0,
          };
          window.touch = "end";

          if (event.touches.length > 0) {
            this.rightClickCallBack(this.start);
          } else if (
            this.start.x == event.changedTouches[0].pageX &&
            this.start.y == event.changedTouches[0].pageY
          ) {
            this.leftClickCallBack(this.move);
          }
        };

        handleTouchMove = (event) => {
          event.preventDefault();
          window.touch = "move";
          var firstTouch = event.changedTouches[0];
          var endX = firstTouch.pageX;
          var endY = firstTouch.pageY;
          var lastMove = this.move;
          var max = Math.max(
            Math.abs(endX - lastMove.x),
            Math.abs(endY - lastMove.y)
          );

          if (max > 1 && (lastMove.x != 0 || lastMove.y !== 0)) {
            this.deltaCallBack({
              x: endX - lastMove.x,
              y: endY - lastMove.y,
            });
          }
          this.move = {
            x: endX,
            y: endY,
          };
        };
      }

      customElements.define("track-pad", Trackpad);
    </script>

    <script>
      function sendClipboardData() {
        try {
          navigator.clipboard.readText().then(function (data) {
            console.log("Copied String ", data);
            sendFormData(createFromData(data, ""));
          }).catch((e) => {
            alert(e.message)
          });

        } catch (e) {
          alert(e.message)
        }
      }

    </script>

    <script>
      let alertDiv = document.getElementById("alert");
      function connectToWebSocket(){
        // alertDiv.style.display = "block"
        if(window.websoc) return;
      let socket = new WebSocket(`wss://${location.hostname}:8765`);

        socket.onopen = function(e) {
          console.log("Web socket connected");
          //  alert("web socket connected");
          alertDiv.style.display = "none"
          window.websoc=socket;
        };
        socket.onmessage = function(event) {
          console.log(`[message] Data received from server: ${event.data}`);
        };

        socket.onclose = function(event) {
          window.websoc= null;
          if (event.wasClean) {
            alertDiv.style.display = "block"
            // alert(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
          } else {
            // e.g. server process killed or network down
            // event.code is usually 1006 in this case
            // alert('[close] Connection died');
            alertDiv.style.display = "block"
          }
        };

        socket.onerror = function(error) {
          alertDiv.style.display = "block"
          // alert(`[error] ${error.message}`);
        };
      }
      connectToWebSocket();
      window.addEventListener("visibilitychange", function(event) {
        connectToWebSocket();
        }, false);
    </script>
    <script>
      if ("serviceWorker" in navigator) {
        window.addEventListener("load", function() {
          navigator.serviceWorker
            .register("/assets/serviceWorker.js")
            .then(res => console.log("service worker registered"))
            .catch(err => console.log("service worker not registered", err))
        })
      }
    </script>
  
</body>

</html>
