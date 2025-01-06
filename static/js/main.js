function scrollToBottom(){
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth"
    });
}

function pop_up(){
    document.querySelector(".popup").style.display="block";
    document.querySelector(".popup-overlay").style.display="block";
}

function pop_back(){
    document.querySelector(".popup").style.display="none";
    document.querySelector(".popup-overlay").style.display="none";
}

function clear(){
    
}