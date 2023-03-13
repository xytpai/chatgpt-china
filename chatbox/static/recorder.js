var chunks = [];
var rec;

navigator.mediaDevices.getUserMedia({audio:true})
    .then(stream => {handlerFunction(stream)})

function handlerFunction(stream) {
    rec = new MediaRecorder(stream);
    rec.ondataavailable = e => {
        chunks.push(e.data);
        if (rec.state == "inactive"){
            let blob = new Blob(chunks, {type:'audio/mp3'});
            var audioElement = document.querySelector('audio');
            audioElement.src = URL.createObjectURL(blob);
            audioElement.controls = true;
            audioElement.autoplay = false;
        }
    }
}

buttonStartRecord.onclick = e => {
    buttonStartRecord.disabled = true;
    buttonStopRecord.disabled = false;
    chunks = [];
    rec.start();
}

buttonStopRecord.onclick = e => {
    buttonStartRecord.disabled = false;
    buttonStopRecord.disabled = true;
    rec.stop();
}
