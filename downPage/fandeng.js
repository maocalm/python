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
            dmLogout("== use bin2String_2 ==");
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
            console.log(e);
        }
        return result;
    }


     hook_Activity.ae.implementation = function(){
            this.a(arguments[0])
            var a = arguments[0];
            send('aaaaaa'+a.albumCoverUrl.value)
            var sss = bin2String(a)
            send('aaaa'+sss)
            var leng = a.length;
            send('aaaa'+leng)

            for(var j = 0; j < a.length; j++) {
                var url = a[j];
                send('aaaaa'+url);
            }

        }
    }
