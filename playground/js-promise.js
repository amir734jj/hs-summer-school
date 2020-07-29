
        setTimeout(function() {
            console.log();
        }, 1000);
        
        // Single thread language and gurantees thread doesn't get blocked
        
        async function foo() {
        
            console.log("Before");

            await bar();
            
            console.log("After");
        }
        
        -------------------------------------
       
        function bar(callback) {
            setTimeout(() => {
                console.log("bar");
                callback();
            }, 5000);
        }


        function foo() {
            console.log("Before");

            var flag = false;
            bar(() => flag = true);
            
            var id = setInterval(function() {
                    console.log("checking ...");
                    if (flag) {
                        console.log("After");
                        clearInterval(id);
                    }
            }, 1000);
        }
        
        -------------------------------------

        function bar(callback) {
            return new Promise((resolve, reject) => {
                setTimeout(() => {
                    console.log("bar");
                    resolve();
                }, 5000);
            });
        }
        
        
         function foo() {
            console.log("Before");
            
            bar().then(() => {
            
                console.log("After");
            });
         }
        
