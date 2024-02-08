import json
import jsonlines
import os

def writeHTML(filename):
    b=os.getcwd() + '/'
    wdata={}
    i=1
    a='''
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,300,600,200&amp;subset=latin,latin-ext" rel="stylesheet" type="text/css" />
    <title>The Physical Impossibility of Death in the Mind of Someone Living</title>
    <link rel="stylesheet" type="text/css" media="screen" href="../../css/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="../../css/font-awesome.min.css" />
    <link rel="stylesheet" type="text/css" media="screen" href="../../css/NewFile.css" />
    <script src="../../js/jquery-3.7.1.min.js"></script>
    <script src="../../js/popper.min.js"></script>
    <script src="../../js/bootstrap.min.js"></script>
</head>
<body>
    <div id="container">       
        <div id="header-wrapper">
            <div id="header">
                <div id="branding">
                    <div id="site-title"><a href="../../Contents.html">The Physical Impossibility of Death in the Mind of Someone Living</a></div>
                </div>
                <div class="dropdown" style="display: inline; float: left;">
                    <a class="btn dropdown-toggle" data-bs-toggle='dropdown' id="dropdownMenu1" data-toggle="dropdown">
                        Menu
                        <span class="caret"></span>
                    </a>
                    <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">
                        <li>
                            <a class="dropdown-item" href="../../Index.html">Home</a>
                        </li>
                        <li>
                            <a class="dropdown-item" href="../../About.html">About</a>
                        </li>
                        <li>
                            <a class="dropdown-item" href="../../Contents.html">Data</a>
                        </li>
                    </ul>
                </div>
                <div class="dropdown" style="display: inline; float: right;">
                    <a class="btn dropdown-toggle" data-bs-toggle='dropdown' id="dropdownMenu1" data-toggle="dropdown" >
                        Media:Weibo
                        <span class="caret"></span>
                    </a>
                    <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">
                        <li>
                            <a class="dropdown-item" href="../../Contents.html">Weibo</a>
                        </li>
                    </ul>
                </div>
            </div> <!-- End header -->
        </div><!-- End header wrapper -->
        <table id="data_table">
            <tbody>
                <tr id="table_head">
                    <th id="table_Created_At">Created At</th>
                    <th id="table_User_Name">User Name</th>
                    <th id="table_Content">Content</th>
                </tr>
            '''
    z='</tbody></table></div> <!-- End container --></body></html>'
    p1='<tr><td><div id=\'created_at\'>'
    p1o='<tr id=\'table_odd\'><td><div id=\'created_at\'>'
    p2="</div></td><td><div id='User Name'>"
    p3="</div></td><td><div id='text_Content'>"
    p4='</div></td></tr>'

    jfname=b+filename[:7]+'/'+filename+'.jsonl'
    hfname=b+filename[:7]+'/'+filename+'.html'
    with open(hfname,'w') as wi:
        wi.write(a)
        wi.close()
        
    with open(jfname,encoding="utf-8") as jsdt:   
        for line in jsdt:
            wdata=json.loads(line)
            with open(hfname,'a',encoding="utf-8") as w:
                if (i % 2) == 0:
                    p=p1o+wdata["created_at"]+p2+wdata["user_name"]+p3+wdata["content"]+p4
                else:
                    p=p1+wdata["created_at"]+p2+wdata["user_name"]+p3+wdata["content"]+p4
                w.write(p)
                w.close()
            i=i+1

    with open(hfname,'a') as wf:
        wf.write(z)
        wf.close()
        
fname=input('输入文件名：')            
writeHTML(fname)
