import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)



js_code = '''
    Java.perform(function(){
        var hook_Activity = Java.use('io.dushu.fandengreader.fragment.AudioFragment');
        var Hook_Activity2 = Java.use('io.dushu.fandengreader.contentactivty.ContentDetailActivity');
        var ContentDetailModel = Java.use('io.dushu.fandengreader.api.ContentDetailModel');
        hook_Activity.a.overload('java.lang.String', 'java.lang.String', 'long', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'long', 'long', 'boolean', 'long', 'long', 'boolean', 'long', 'boolean', 'boolean').implementation = function(){
            //this.a('java.lang.String', 'java.lang.String', 'long', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'long', 'long', 'boolean', 'long', 'long', 'boolean', 'long', 'boolean', 'boolean');
            this.a.overload('java.lang.String', 'java.lang.String', 'long', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'long', 'long', 'boolean', 'long', 'long', 'boolean', 'long', 'boolean', 'boolean').apply(this,arguments)

            send("MacByte1:"+this.p.value);
            send("MacByte2:"+this.q.value);
            send("MacByte3:"+this.n.value);
            send("MacByte4:"+this.o.value);
            send("MacByte5:"+this.r.value);
            send("MacByte6:"+this.s.value);
            send("MacByte7:"+this.t.value);
            send("MacByte8:"+this.E.value);
            send("MacByte9:"+this.F.value);
            send('aaaaa');

            //var instance = Hook_Activity2.$new();
            //var String_java = Java.use('java.lang.String');
            //var str= String_java.valueOf(instance.albumCoverUrl.value);
            var instance  = this.getActivity()
            var mode = instance.U
            var packageInfo = Java.cast(mode, ContentDetailModel);
            var pkg = packageInfo.albumCoverUrl.value
            send('aaaaa  ' +pkg);

        }
    });
'''

js_code3 = '''
    function bin2String(array) {
        if (null == array) {
            return "null";
        }
        var result = "";
        try {
            var String_java = Java.use('java.lang.String');
            result = String_java.$new(array);
        }
        catch (e) {
            send("== use bin2String_2 ==");
            result = bin2String_2(array);
        }

        return result;
    }

    function bin2String_2(array) {
        var result = "";
        try {
            var tmp = 0;
            for (var i = 0; i < array.length; i++) {
                tmp = parseInt(array[i]);
                if ( tmp == 0xc0
                    || (tmp < 32 && tmp != 10)
                    || tmp > 126 )  {
                    return result;
                }  // 不是可见字符就返回了, 换行符除外
                result += String.fromCharCode(parseInt(array[i].toString(2), 2));
            }
        }
        catch (e) {
            send('cuosu')
            console.log(e);
        }
        return result;
    }

    Java.perform(function(){
        var hook_Activity = Java.use('io.dushu.fandengreader.contentactivty.ContentDetailActivity');
        var ContentDetailModel = Java.use('io.dushu.fandengreader.api.ContentDetailModel');

        hook_Activity.ae.implementation = function(){
            this.ae()

            var mode = this.p.value;
            //var packageInfo = Java.cast(mode ,ContentDetailModel);
            //var pkg = packageInfo.albumCoverUrl.value;
            send('aaaaa  ' +mode);

            // var sss = bin2String(a)
            // send('aaaa'+sss)
            // var leng = a.length;
            // send('aaaa'+leng)
            //
            // for(var j = 0; j < a.length; j++) {
            //     var url = a[j];
            //     send('aaaaa'+url);
            // }

        }
    });
'''

js_code2 = """
    Java.perform(function() {
		var log = Java.use("android.util.Log");
		log.d.overload('java.lang.String', 'java.lang.String').implementation = function (var0, var1) {
			console.log("[*] Debug log displayed with TAG: " + var0 + " and VALUE: " + var1 + "\\n");
			this.d(var0, var1);
		};

		log.d.overload('java.lang.String', 'java.lang.String', 'java.lang.Throwable').implementation = function (var0, var1, var2) {
			console.log("[*] Debug log displayed with TAG: " + var0 + " and VALUE: " + var1 + "\\n");
			this.d(var0, var1, var2);
		};

		log.e.overload('java.lang.String', 'java.lang.String').implementation = function (var0, var1) {
			console.log("[*] Error log displayed with TAG: " + var0 + " and VALUE: " + var1 + "\\n");
			this.e(var0, var1);
		};

		log.e.overload('java.lang.String', 'java.lang.String', 'java.lang.Throwable').implementation = function (var0, var1, var2) {
			console.log("[*] Error log displayed with TAG: " + var0 + " and VALUE: " + var1 + "\\n");
			this.e(var0, var1, var2);
		};

		log.i.overload('java.lang.String', 'java.lang.String').implementation = function (var0, var1) {
			console.log("[*] Information log displayed with TAG: " + var0 + " and VALUE: " + var1 + "\\n");
			this.i(var0, var1);
		};

		log.i.overload('java.lang.String', 'java.lang.String', 'java.lang.Throwable').implementation = function (var0, var1, var2) {
			console.log("[*] Information log displayed with TAG: " + var0 + " and VALUE: " + var1 + "\\n");
			this.i(var0, var1, var2);
		};

		log.v.overload('java.lang.String', 'java.lang.String').implementation = function (var0, var1) {
			console.log("[*] Verbose log displayed with TAG: " + var0 + " and VALUE: " + var1 + "\\n");
			this.v(var0, var1);
		};

		log.v.overload('java.lang.String', 'java.lang.String', 'java.lang.Throwable').implementation = function (var0, var1, var2) {
			console.log("[*] Verbose log displayed with TAG: " + var0 + " and VALUE: " + var1 + "\\n");
			this.v(var0, var1, var2);
		};

		log.w.overload('java.lang.String', 'java.lang.String').implementation = function (var0, var1) {
			console.log("[*] Warning log displayed with TAG: " + var0 + " and VALUE: " + var1 + "\\n");
			this.w(var0, var1);
		};

		log.w.overload('java.lang.String', 'java.lang.String', 'java.lang.Throwable').implementation = function (var0, var1, var2) {
			console.log("[*] Warning log displayed with TAG: " + var0 + " and VALUE: " + var1 + "\\n");
			this.w(var0, var1, var2);
		};

		log.wtf.overload('java.lang.String', 'java.lang.String').implementation = function (var0, var1) {
			console.log("[*] What a terrible failure log displayed with TAG: " + var0 + " and VALUE: " + var1 + "\\n");
			this.wtf(var0, var1);
		};


		log.wtf.overload('java.lang.String', 'java.lang.String', 'java.lang.Throwable').implementation = function (var0, var1, var2) {
			console.log("[*] What a terrible failure log displayed with TAG: " + var0 + " and VALUE: " + var1 + "\\n");
			this.wtf(var0, var1, var2);
		};
	});
"""

session = frida.get_usb_device().attach("io.dushu.fandengreader")
script = session.create_script(js_code)
script.on('message', on_message)
script.load()
sys.stdin.read()
