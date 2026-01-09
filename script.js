const SECRET_FLAG = "LNM{N07_H3R3}";

function checkFlag() {
    const userInput = document.getElementById("flagInput").value.trim();
    const resultArea = document.getElementById("resultArea");
    const flagDisplay = document.getElementById("flagValue");

    if (userInput === SECRET_FLAG) {
        resultArea.classList.remove("hidden");
        flagDisplay.innerText = SECRET_FLAG;
    } else {
        alert("Integrity check failed. Invalid sequence.");
    }
}

function copyToClipboard() {
    const flag = document.getElementById("flagValue").innerText;
    navigator.clipboard.writeText(flag).then(() => {
        const copyBtn = document.getElementById("copyBtn");
        copyBtn.innerText = "Copied!";
        copyBtn.style.background = "#fff";
        
        // Reset button after 2 seconds
        setTimeout(() => {
            copyBtn.innerText = "Copy";
            copyBtn.style.background = "#00ff41";
        }, 2000);
    }).catch(err => {
        console.error('Error copying text: ', err);
    });
}