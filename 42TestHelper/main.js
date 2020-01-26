;
'use strict';

function toJava() {
    
    const lines = document.getElementById("42-code").value.split("\n");
    const newLines = ["@Test"];
    newLines.push("public void " + "PLACEHOLDER_METHOD_NAME" + "() {");
    newLines.push("\t tp(\"{\"");

    lines.forEach(e => {

        let t = e.split("");

        for (let i = 0; i <= e.length; ++i) {
            if (t[i] === "\"") {
                t.splice(i, 0, "\\");

                i++;
            }
        }

        t = t.join("");

        newLines.push("\t ,\"" + t.trim() + "\"");
    });

    newLines.push(",\"}\");");
    newLines.push("}");

    document.getElementById("java-code").value = newLines.join("\n");
}

function to42() {
    let lines = document.getElementById("java-code").value.split("\n");
    
    lines.pop();
    lines.pop();
    
    lines.splice(0, 1);
    lines.splice(0, 1);

    const newLines = [];

    lines.forEach(e => {
        e = e.trim();

        if (!(e === "tp(\"{reuse L42.is/AdamTowel02\"")) {
            newLines.push(e.substring(2, e.length - 1));
        }

        else {
            newLines.push(e.substring(5, e.length - 1));
        }

    });

    const t = newLines.pop();
    if (!(t === "}\")")) {
        newLines.push(t);
    }

    document.getElementById("42-code").value = newLines.join("\n");
}