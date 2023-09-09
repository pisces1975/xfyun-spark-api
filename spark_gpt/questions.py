q_writeCode1 =''' 请用python实现一个贪食蛇程序，控制按键是asdwx。'''
q_business = '''请解释一下存款业务都有什么样的计息方式'''
q_writeCode2 = '''输入是LIST，每个元素是ID，parent_id，content，标识一篇文章，ID是本文的ID，parent_id是它的上级文章的ID，写python程序产生一个文章的结构树'''
q_explainCode_python = '''请解释代码
def main(appid, api_key, api_secret, Spark_url, domain, question):
    # print("星火：")
    wsParam = Ws_Param(appid, api_key, api_secret, Spark_url)
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()
    ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close, on_open=on_open)
    ws.appid = appid
    ws.question = question
    ws.domain = domain
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
'''
q_explainCode_pom = '''请解释代码
stage('build') {
            steps {
                script {
                    modulesSelect.each{k,v ->
                      def git_url = v.url
                      
                        if(v.isChecked){
                            
                            dir(k){
                        
                               git branch: params.branch, credentialsId: '167fc9c5-d1cf-49c0-965b-a1d5c26cea0b', url: git_url 
                               def fpath = ""
                               if (v.config) {
                                   fpath = v.config
                               }
                               print(params.environ_select+"------------>")
                               sh """
                                  git checkout ${params.branch}
                               """
                               
                               if (params.environ_select == 'wlsk-test'){
                                   withCredentials([usernamePassword(credentialsId: '922fd59d-ffb7-4d32-8e4e-7584152a9a7a', passwordVariable: 'gitlab_user_password', usernameVariable: 'gitlab_user_name')]) {
                                        def test_url = v.url.replace('http://','http://'+gitlab_user_name+':'+gitlab_user_password+'@')
                                       sh """
                                          git config --local user.email "zhangjingui@nstc.com.cn"
                                          git config --local user.name "zhangjgnstc"
                                          git merge ${k}-SNAPSHOTS
                                          git push ${test_url} release:release 
                                       """
                                    }
                               }
                               
                               sh """
                                    mvn --version
                                    node -v
                                    which node
                                    which npm
                                    export PYTHONUNBUFFERED=1
                                    python -u /data/script/CI_CD_v2.pyc -s build ${fpath} -n dev
                                """
                            }
                            
                               
                        }
                    }
                }
            }
        }

'''
q_transaltion = '''请翻译为中文
2. Usage Requirements
(a) Use of Services. You may access, and we grant you a non-exclusive right to use, the Services in accordance with these Terms. 
You will comply with these Terms and all applicable laws when using the Services. We and our affiliates own all rights, title, 
and interest in and to the Services.

(b) Feedback. We appreciate feedback, comments, ideas, proposals and suggestions for improvements. If you provide any of these things, 
we may use it without restriction or compensation to you.

(c) Restrictions. You may not (i) use the Services in a way that infringes, misappropriates or violates any person’s rights;
 (ii) reverse assemble, reverse compile, decompile, translate or otherwise attempt to discover the source code or underlying 
 components of models, algorithms, and systems of the Services (except to the extent such restrictions are contrary to applicable law); 
 (iii) use output from the Services to develop models that compete with OpenAI; (iv) except as permitted through the API, use any 
 automated or programmatic method to extract data or output from the Services, including scraping, web harvesting, or web data extraction;
   (v) represent that output from the Services was human-generated when it is not or otherwise violate our Usage Policies; 
   (vi) buy, sell, or transfer API keys without our prior consent; or (vii), send us any personal information of children under 
   13 or the applicable age of digital consent. You will comply with any rate limits and other requirements in our documentation. 
   You may use Services only in geographies currently supported by OpenAI.
'''