import os
import glob

directory = "/home/mrdas/WINSTA-AI/WINSTA-AI-V3/www.rameshdas.dev/"
html_files = glob.glob(os.path.join(directory, "*.html"))

clarity_script = """
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "x6pgyo2rbk");
</script>
"""

count = 0
for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "clarity.ms/tag" not in content and "x6pgyo2rbk" not in content:
        # Inject right before </head>
        if "</head>" in content:
            new_content = content.replace("</head>", clarity_script + "</head>")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            
print(f"Successfully injected Microsoft Clarity script into {count} HTML files.")
