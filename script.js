// Timestamp Update
function updateTimestamp() {
    const timestamp = document.getElementById('timestamp');
    const now = new Date();
    
    // Format: YYYY.MM.DD HH:MM:SS
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    
    timestamp.textContent = `${year}.${month}.${day} ${hours}:${minutes}:${seconds}`;
}

// Update timestamp every second
updateTimestamp();
setInterval(updateTimestamp, 1000);

// Subtle console message (Easter egg for developers)
console.log('%c>>> SYSTEM READY <<<', 'color: #00ff00; font-family: monospace; font-size: 14px;');
console.log('%cBuilt for expansion. Python-ready architecture.', 'color: #ffffff; font-family: monospace; font-size: 12px;');
