setImmediate(function() {
    console.log("[*] Starting script");
    Java.perform(function() {
        Java.choose("android.widget.EditText", {
        "onMatch":function(instance) {
            console.log("[*] Instance found");
        },
        "onComplete":function() {
            console.log("[*] Finished heap search")
        }
        });
    });
});