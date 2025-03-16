<div align="center">
  <img width="250" height="250" src="assets/PRINTClogo.svg">
  <br><br>
  <kbd>
    <a href="#">
      <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff" alt="Python">
    </a>
  </kbd>
  &nbsp;&nbsp;
  <kbd>
    <a href="https://github.com/EpitaphNewell">
      <img src="https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white" alt="GitHub">
    </a>
  </kbd>
  &nbsp;&nbsp;
  <kbd>
    <a href="https://opensource.org/licenses/MIT">
      <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
    </a>
  </kbd>
</div>

<h1 align="center">Color Print (PrintC)</h1>
<p align="center"><b>This is a library that allows you to output colored notifications to the console</b></p>

> [!Warning]\
> For the library to function correctly, a terminal that supports a color display is required!

> [!Tip]\
> You can use this with logger,
> you can also take {er} as a basis and create your own colored messages for the logger




<h1 align="center">Image Gallery</h1>

<details>
<summary>Click to open/close gallery</summary>

<div style="display: flex; flex-direction: column; align-items: flex-start; gap: 20px; margin-top: 15px;">
  &nbsp;&nbsp;
  <div>
    <img src="assets/pong.png" alt="Ping Pong" style="width: 390px; height: auto;">
  </div>
  &nbsp;&nbsp;
  <div>
    <img src="assets/pong2.png" alt="Path" style="width: 400px; height: auto;">
  </div>
  &nbsp;&nbsp;
  <div>
    <img src="assets/pong3.png" alt="Cube" style="width: 180px; height: auto;">
  </div>
</div>

</details>


<h1 align="center">Color Syntax Guide</h1>
<details>
<summary>Click to open/close syntax guide</summary>
<div style="display: flex; flex-direction: column; align-items: flex-start; gap: 20px; margin-top: 15px;">
  &nbsp;&nbsp;
  <div>
    <h3>Basic Color Tags</h3>
    <hr></hr>
    <code>{re}</code> - Red text<br>
    <code>{yl}</code> - Yellow text<br>
    <code>{gr}</code> - Green text<br>
    <code>{bl}</code> - Blue text<br>
    <code>{rs}</code> - Reset color (return to default)
  </div>
  &nbsp;&nbsp;
  <div>
    <h3>Error Format</h3>
    <hr></hr>
    <code>{er}</code> - Formats an error message in red with [ERROR] prefix
  </div>
  &nbsp;&nbsp;
  <div>
    <h3>Usage Examples</h3>
    <hr></hr>
    <span></span>
    <code>printc("{gr}Success!{rs}")</code>
    <br><br>
    <code>printc("{re}Warning: {yl}Low disk space{rs}")</code>
    <br><br>
    <code>printc("{er}", "File not found")</code>
  </div>
</div>
</details>
