import json
from bs4 import BeautifulSoup


html_content = """
<div class="container">
		<h1>GCSE Vocabulary</h1>
		<p>Starting in 2025 BSL will be offered as a GCSE subject. Below is a list of the English translations of 1000 commonly used BSL signs that students are expected to know. In this online dictionary these words are marked with a <span class="label label-info" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Vocabulary that students taking BSL at GCSE level are expected to know.">GCSE vocabulary</span> label.</p>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Verbs</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/accept">accept</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/arrive">arrive</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/ask">ask</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/believe">believe</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/born">born</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/break">break</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/bring">bring</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/buy">buy</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/change">change</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/come">come</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/communicate">communicate</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/continue">continue</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cook">cook</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/do">do</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/drink">drink</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/drive">drive</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/drove">drove</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/eat">eat</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/encourage">encourage</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/enter">enter</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/exist">exist</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/explain">explain</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/feel">feel</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/find">find</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/finish">finish</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fish">fish</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fix">fix</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fly">fly</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/follow">follow</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/forget">forget</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/get">get</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/give">give</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/go">go</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/grow-up">grow up</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/happen">happen</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/have">have</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hear">hear</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/help">help</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hold">hold</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/interpret">interpret</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/involve">involve</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/join">join</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/kick">kick</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/know">know</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/know-not">know not</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/laugh">laugh</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/learn">learn</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/leave">leave</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/leave-alone">leave-alone</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/like">like</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/live">live</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/look">look</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/look-after">look after</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/love">love</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/make">make</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/marry">marry</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/mean">mean</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/meet">meet</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/mix">mix</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/move">move</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/negotiate">negotiate</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/pay">pay</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/pick">pick</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/play">play</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/progress">progress</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/put-aside">put aside</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/read">read</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/remember">remember</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/saw">saw</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/say">say</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/search">search</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/see">see</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/send-text">send text</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/shift">shift</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/shock">shock</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/show">show</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sign">sign</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sign-chat">sign chat</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sit">sit</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sleep">sleep</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/smell">smell</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/speak">speak</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/stand">stand</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/start">start</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/stay">stay</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/stop">stop</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/take">take</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/talk">talk</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/teach">teach</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/telephone">telephone</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/tell">tell</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/think">think</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/travel">travel</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/try">try</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/understand">understand</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/use">use</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/visit">visit</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/wait">wait</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/wake-up">wake up</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/walk">walk</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/want">want</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/watch">watch</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/wonder">wonder</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/work">work</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/write">write</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Objects</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/airplane">airplane</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/airport">airport</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/ball">ball</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/bed">bed</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/bicycle">bicycle</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/blanket">blanket</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/boat">boat</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/body">body</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/book">book</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/broadband">broadband</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/bus">bus</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/bus-pass">bus pass</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cable">cable</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/car">car</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/ceiling-light">ceiling light</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/chest-of-drawers">chest of drawers</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/computer">computer</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cup">cup</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cupboard">cupboard</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/duvet">duvet</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/flat">flat</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fork">fork</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/google">google</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/group">group</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hair">hair</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hairdryer">hairdryer</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hand">hand</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/helicopter">helicopter</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/house">house</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/internet">internet</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/kettle">kettle</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/kilogram">kilogram</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/knife">knife</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/lift">lift</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/lorry">lorry</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/microwave">microwave</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/mile">mile</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/mobile-phone">mobile phone</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/mobile-telephone">mobile telephone</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/money">money</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/moon">moon</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/motorbike">motorbike</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/mountain">mountain</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/penny">penny</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/pillow">pillow</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/plate">plate</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/pound">pound</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/railway-station">railway station</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/river">river</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sat-nav">sat nav</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/scissors">scissors</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sea">sea</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sheet">sheet</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sky">sky</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/spoon">spoon</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/stairs">stairs</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/star">star</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sun">sun</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/table-lamp">table lamp</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/taxi">taxi</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/television">television</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/ticket">ticket</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/toaster">toaster</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/toothbrush">toothbrush</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/train">train</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/tram">tram</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/tube">tube</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/uber">uber</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/ufo">ufo</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/vacuum-cleaner">vacuum cleaner</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/wallet">wallet</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/water">water</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/way">way</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/wifi">wifi</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Numerals</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/billion">billion</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/eight">eight</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/eighteen">eighteen</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/eighteenth">eighteenth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/eighth">eighth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/eighty">eighty</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/eleven">eleven</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/eleventh">eleventh</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fifteen">fifteen</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fifteenth">fifteenth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fifth">fifth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fifty">fifty</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/first-ordinal">first ordinal</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/five">five</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/forty">forty</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/four">four</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fourteen">fourteen</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fourteenth">fourteenth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fourth">fourth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hundred">hundred</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hundredth">hundredth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/million">million</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/nine">nine</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/nineteen">nineteen</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/nineteenth">nineteenth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/ninety">ninety</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/ninth">ninth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/one">one</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/second">second</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/seven">seven</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/seventeen">seventeen</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/seventeenth">seventeenth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/seventh">seventh</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/seventy">seventy</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/six">six</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sixteen">sixteen</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sixteenth">sixteenth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sixth">sixth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sixty">sixty</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/ten">ten</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/tenth">tenth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/third">third</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/thirteen">thirteen</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/thirteenth">thirteenth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/thirty">thirty</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/thousand">thousand</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/thousandth">thousandth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/three">three</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/twelfth">twelfth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/twelve">twelve</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/twentieth">twentieth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/twenty">twenty</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/two">two</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/zero">zero</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Adjectives and Adverbs</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/again">again</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/all">all</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/always">always</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/bad">bad</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/best">best</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/better">better</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/big">big</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/different">different</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/easy">easy</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/enough">enough</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/every">every</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/evil">evil</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fantastic">fantastic</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/far">far</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fed-up">fed up</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/few">few</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/first">first</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/full">full</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/funny">funny</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/good">good</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/half">half</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/happy">happy</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hard">hard</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/high">high</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/ill">ill</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/interesting">interesting</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/last">last</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/little">little</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/lots">lots</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/many">many</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/medical">medical</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/more">more</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/most">most</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/new">new</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/old">old</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/other">other</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/painful">painful</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/patient">patient</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/perfect">perfect</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/plenty">plenty</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/ready">ready</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/real">real</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/really">really</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/right">right</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/same">same</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/small">small</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/some">some</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/still">still</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/strict">strict</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/strong">strong</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/tired">tired</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/top">top</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/true">true</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/very">very</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/well">well</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/worse">worse</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/wrong">wrong</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/young">young</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Places</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/belfast">Belfast</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/birmingham">Birmingham</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/blackpool">Blackpool</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/brighton">Brighton</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/china">China</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/denmark">Denmark</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/dublin">Dublin</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/edinburgh">Edinburgh</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/england">England</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/finland">Finland</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/france">France</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/gaelic">Gaelic</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/germany">Germany</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/glasgow">Glasgow</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/greece">Greece</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/india">India</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/ireland">Ireland</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/italy">Italy</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/japan">Japan</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/leeds">Leeds</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/leicester">Leicester</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/liverpool">Liverpool</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/london">London</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/manchester">Manchester</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/northern-ireland">Northern Ireland</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/norway">Norway</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/pakistan">Pakistan</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/paris">Paris</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/portsmouth">Portsmouth</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/portugal">Portugal</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/rome">Rome</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/russia">Russia</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/scotland">Scotland</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/spain">Spain</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sweden">Sweden</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/usa">Usa</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/wales">Wales</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/welsh">Welsh</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/area">area</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/bank">bank</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/café">café</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/club">club</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/english">english</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/farm">farm</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/home">home</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hospital">hospital</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/pub">pub</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/room">room</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/shop">shop</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/world">world</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Animals</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/bat">bat</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/bird">bird</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/butterfly">butterfly</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cat">cat</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/chicken">chicken</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cockerel">cockerel</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cow">cow</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/deer">deer</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/dog">dog</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/duck">duck</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/elephant">elephant</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/frog">frog</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/giraffe">giraffe</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/goat">goat</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/horse">horse</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/insect">insect</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/lion">lion</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/mouse">mouse</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/pig">pig</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/rhino">rhino</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sheep">sheep</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/snake">snake</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/tiger">tiger</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>People</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/actor">actor</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/aunt">aunt</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/baby">baby</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/baker">baker</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/boss">boss</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/both-of-us">both of us</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/boy">boy</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/boyfriend">boyfriend</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/brother">brother</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/builder">builder</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/carpenter">carpenter</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/child">child</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/children">children</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cook">cook</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cousin">cousin</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/daughter">daughter</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/dentist-interpreter">dentist interpreter</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/doctor">doctor</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/electrician">electrician</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/family">family</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/father">father</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/friend">friend</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/girl">girl</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/girlfriend">girlfriend</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/grandfather">grandfather</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/grandmother">grandmother</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hairdresser">hairdresser</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/king">king</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/lady">lady</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/man">man</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/monster">monster</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/mother">mother</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/nephew">nephew</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/niece">niece</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/nurse">nurse</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/parents">parents</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/people">people</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/person">person</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/plumber">plumber</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/prince">prince</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/princess">princess</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/queen">queen</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/robot">robot</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/singer">singer</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sister">sister</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/son">son</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/spouse">spouse</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/staff">staff</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/teacher">teacher</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/translator">translator</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/twins">twins</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/uncle">uncle</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/witch">witch</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/wizard">wizard</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/woman">woman</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Food</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/afternoon-meal">afternoon meal</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/apple">apple</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/bacon">bacon</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/banana">banana</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/beer">beer</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/biscuit">biscuit</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/bread">bread</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/breakfast">breakfast</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/burger">burger</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cake">cake</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/carrot">carrot</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cheese">cheese</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cherry">cherry</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/chips">chips</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/chocolate">chocolate</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/coffee">coffee</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cola">cola</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cream">cream</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/crisps">crisps</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/egg">egg</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/evening-meal">evening meal</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fish">fish</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/food">food</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/grape">grape</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/gravy">gravy</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/ice-cream">ice cream</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/meat">meat</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/midday-meal">midday meal</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/milk">milk</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/noodles">noodles</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/orange">orange</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/pie">pie</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/pizza">pizza</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/potato">potato</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/recipe">recipe</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/rice">rice</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/salad">salad</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sausage">sausage</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/snack">snack</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/strawberry">strawberry</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sugar">sugar</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/takeaway">takeaway</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/tea">tea</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/tomato">tomato</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/wine">wine</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Modal verbs</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/can">can</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cant">can't</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/must">must</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/should">should</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/will">will</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/wont">won't</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Questions</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/how">how</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/how-far">how far</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/how-many">how many</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/how-much">how much</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/how-old">how old</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/what">what</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/when">when</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/where">where</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/which">which</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/why">why</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Clothing</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/belt">belt</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/boots">boots</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/bra">bra</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/dress">dress</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/eyeglasses">eyeglasses</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/gloves">gloves</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hat">hat</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hoodie">hoodie</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/jacket">jacket</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/jumper">jumper</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/necklace">necklace</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/scarf">scarf</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/shirt">shirt</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/shoes">shoes</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/skirt">skirt</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/socks">socks</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/tee-shirt">tee-shirt</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/tie">tie</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/trousers">trousers</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/underwear">underwear</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/vest">vest</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/watch">watch</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Calendar time</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/age">age</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/april">april</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/august">august</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/autumn">autumn</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/date">date</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/day">day</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/december">december</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/february">february</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fortnight">fortnight</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/friday">friday</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hour">hour</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/january">january</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/july">july</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/june">june</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/march">march</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/may">may</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/minute">minute</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/monday">monday</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/month">month</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/morning">morning</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/night">night</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/november">november</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/october">october</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/saturday">saturday</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/september">september</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/spring">spring</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/summer">summer</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sunday">sunday</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/thursday">thursday</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/today">today</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/tuesday">tuesday</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/wednesday">wednesday</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/week">week</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/winter">winter</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/year">year</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Sports</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/american-football">american football</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/ballet">ballet</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/basketball">basketball</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/box">box</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/ceilidh">ceilidh</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/compete">compete</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/competition">competition</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cricket">cricket</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/dance">dance</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/deaflympics">deaflympics</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/field">field</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/football">football</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/goal">goal</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/golf">golf</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hockey">hockey</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/judge">judge</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/keep-fit">keep fit</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/league">league</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/medal">medal</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/netball">netball</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/paralympics">paralympics</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/partner">partner</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/rock-and-roll">rock and roll</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/rugby">rugby</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/rules">rules</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/run">run</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/score">score</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/skating">skating</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/skiing">skiing</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sport">sport</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/stadium">stadium</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/swim">swim</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/team">team</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/tennis">tennis</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/torch">torch</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>School terminology</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/6th-form">6th form</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/art">art</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/biology">biology</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/chemistry">chemistry</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/class">class</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/college">college</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/computing">computing</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/essay">essay</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/examination">examination</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/geography">geography</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/history">history</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/homework">homework</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/lesson">lesson</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/maths">maths</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/music">music</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/physics">physics</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/poetry">poetry</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/school">school</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/science">science</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/theatre">theatre</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/university">university</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Function terms</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/about">about</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/and">and</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/because">because</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/but">but</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/if">if</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/in">in</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/next">next</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/on">on</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/or">or</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/over">over</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/through">through</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/under">under</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/with">with</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Time related terms</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/after">after</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/before">before</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/later-on">later on</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/long-time-ago">long time ago</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/now">now</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/only">only</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/past">past</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/then">then</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/time">time</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/timespan">timespan</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/today">today</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/tomorrow">tomorrow</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/yesterday">yesterday</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Colours</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/black">black</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/blue">blue</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/brown">brown</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/green">green</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/grey">grey</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/pink">pink</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/red">red</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/white">white</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/yellow">yellow</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Abstract concepts</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/action">action</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/amazon">amazon</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/association">association</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/course">course</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/culture">culture</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/education">education</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/everything">everything</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/experience">experience</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fantasy">fantasy</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/film">film</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/fingerspelling">fingerspelling</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/holiday">holiday</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/job">job</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/language">language</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/life">life</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/murder">murder</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/name">name</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/netflix">netflix</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/poem">poem</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/police">police</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/problem">problem</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/robbery">robbery</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/sign">sign</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/something">something</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/story">story</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/thriller">thriller</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/title">title</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/word">word</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Deaf related terms</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cochlear-implant">cochlear implant</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/deaf">deaf</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hard-of-hearing">hard of hearing</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hearing">hearing</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/hearing-aid">hearing aid</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/oral">oral</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Equality</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/asian">asian</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/bisexual">bisexual</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/black-race">black race</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/brown">brown</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/gay">gay</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/lesbian">lesbian</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/lgbtqia">lgbtqia</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/non-binary">non-binary</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/queer">queer</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/race">race</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/rainbow">rainbow</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/transgender">transgender</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Name signs</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/winston-churchill">Winston Churchill</a>
                        </div>
                                    </div>
            </div>
                    <div class="col-md-12">
                <div class="row">
                    <h3>Pandemic</h3>
                                                                <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/cough">cough</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/covid">covid</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/lockdown">lockdown</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/mask">mask</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/pandemic">pandemic</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/social-distancing">social distancing</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/test">test</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/test-swab">test swab</a>
                        </div>
                                            <div class="col-md-2 col-sm-3 col-xs-6">
                            <a href="/sign/vaccine">vaccine</a>
                        </div>
                                    </div>
            </div>
        
	</div>
"""

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Extract all <a> tags
a_tags = soup.find_all('a')

# Create a dictionary to store the mappings
sign_mappings = {}

# Loop through each <a> tag and extract the text and href attribute
for tag in a_tags:
    text = tag.get_text(strip=True)
    href = tag.get('href')
    sign_mappings[text] = href

# Rename caf\u00e9 with cafe in the dictionary
sign_mappings['cafe'] = sign_mappings.pop('caf\u00e9')
# Change the value of cafe to /sign/cafe
sign_mappings['cafe'] = '/sign/cafe'


# Write the dictionary to a JSON file
with open('SignMappings/words.json', 'w') as json_file:
    json.dump(sign_mappings, json_file, indent=4)

print("JSON file 'SignMappings/words.json' created successfully.")
