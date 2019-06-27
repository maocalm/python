import frida
import sys

# package_name = "com.androidtools.miniantivirus"
# package_name = "com.mwr.example.sieve"
package_name = "io.dushu.fandengreader"


def get_messages_from_js(message, data):
    print(message)


def getcurrentInstance():
    hook_code = """
    setImmediate(function() {
        console.log("[*] Starting script");
        Java.perform(function() {
            var ContentDetailModel = Java.use('io.dushu.fandengreader.api.ContentDetailModel');
            Java.choose("io.dushu.fandengreader.api.ContentDetailModel", {
            "onMatch":function(instance) {
                console.log("[*] Instance found: " + instance.mediaUrls.toString());
                //var packageInfo = Java.cast(instance ,ContentDetailModel);
                var pkg = instance.albumCoverUrl.value;
                console.log("pkg found :" + pkg)
                for(var j = 0; j < instance.mediaUrls.length; j++) {
                    var url = instance.mediaUrls[j];
                     //send('aaaaa'+url);
                    console.log("url found :" + url)
                }
            },
            "onComplete":function() {
                console.log("[*] Finished heap search")
            }
            });
        });
    });
    """
    return hook_code


def instrument_debugger_checks():
    hook_code = """
    Java.perform(function(){
        Java.enumerateLoadedClasses({
            onMatch: function(className) {
                send(className);
            },onComplete:function(){
                send("done");
            }
        });
    });
    """
    return hook_code


process = frida.get_device_manager().enumerate_devices()[-1].attach(package_name)
# file = open("printclass.js")
# jsStr = file.read()
script = process.create_script(getcurrentInstance())
script.on('message', get_messages_from_js)
script.load()
sys.stdin.read()
