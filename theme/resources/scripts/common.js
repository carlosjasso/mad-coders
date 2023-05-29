document.addEventListener("DOMContentLoaded", DOMContentLoadedHandler);

function DOMContentLoadedHandler() {
    ToggleTimestamps();
}

function ToggleTimestamps() {
    Array.from(document.getElementsByClassName("article__timestamp")).forEach(element => {
        Array.from(element.getElementsByClassName("article__timestamp__value")).forEach(child => {
            const timestamp = new Date(child.innerHTML);
            child.innerHTML = `${timestamp.toLocaleDateString()} ${timestamp.toLocaleTimeString()}`;
        })
        
        if (element.classList.contains("hidden")) {
            element.classList.remove("hidden");
        }
    });
}