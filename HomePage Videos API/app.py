from typing import Union
from fastapi import FastAPI
from random import choices

app = FastAPI()

total_videos_list=['WomQr-jRO1c', 'qTEag3J1ebY', 'ufBbWIyKY2E', 'tN6oJu2DqCM', 'T-dzgrlgmm0', 'imqiYWidUIA', 'OHvfgaDl-yY', 'YrtFtdTTfv0', 'Ixsr2RyZcv4', 'bmmQA8A-yUA', 'cxgAN7T3rq8', 'mEsleV16qdo', 'mCjRYS1Wr0Q', 'DJtX3S7qx2s', 'hHjmr_YOqnU', '2ZLl8GAk1X4', 'tM6OOJt0S2Y', '_7UQPve99r4', 'o5t7PxRJSXk', 'vb7CgDcA_6U', 'vDJq3QavcaQ', 'nKovSmd5DWY', 'YdWkUdMxMvM', '5rNk7m_zlAg', '5ZdHfJVAY-s', 'OwjKN9_NqPI', 'e2nkq3h1P68', 'Jdc0i7RcBv8', 'BAregq0sdyY', 'KkC_wYM_Co4', 't8QuD3s9GsI', '8hW-OjwpwMk', 'jSVVsD3H7zs', 'g14Rkur1SCw', 'ROCEdC_lN9Y', '2BPDwDoiw3E', 'LMtUAg6K2_E', 'He4V-qn188k', 'jnXoWCJIlUQ', 'ZVllQ9BEt2U', 'B5usn2_XQVE', 'zgnFyw19neg', 'mzliUdPTKxc', '4fW5AI7UGS4', 'Lk2cefL1dyw', 'GrX4WfT5FI4', '6jkmjiuJHfI', 'MPVEKQmG3HE', 'a7RAZ4CPz88', 'CdmB0i_P05w', 'Uf0oASEHTvo', 'BrwwQbyWFo8', 'gPbZzBdlbuo', 'fxnllJthf3M', 'SffSAkgn3ho', 'Xu-9hLN4-NY', '8l0a15pic9Q', 'y4LxSxKsjBE', 'j8JUhfbMVSU', 'G7vSghI7f0c', 'mmtcpK_5rb8', 'ImBqsE2exGo', 'TWnl0SpcAac', 'wo5Lj6OUlRc', '8Xed2Fhd9FU', 'y4WS8OvIapU', 'Jl9OKQ92SJU', '0G3_Fxztpzw', '4XTsAAHW_Tc', 'Nc9NmS5kEjU', 'xrHMof4bLM8', 'CScxy0294SE', 'FBkj-4lzEnU', 'laPmEW913_k', 'xWLxhF3b5P8', 'pJf1iVGTmxQ', 'SHqvb69Qy70', 'hPzlKHFc3Y4', '8JfJLhbWNbQ', '_C-ARJemnC0', 'VNrF8ugTUkI', 'rrfRRllt4c4', 'nZ-9wheuWME', 'OX9kLcVIuxs', '-jCFJKQCWg8', 'nBUfLL4HgIo', 'OUKBP64yZyk', 'Nw2x0dGXBYw', '39FA26nKlOw', '7v2OnUti2eM', 'L0izVqsaxLI', 'qdyt8UO-MqM', 'adNHZVBd284', 'BwKfjzxTGXI', 'DvZuJeTHWaw', 'j_rCDc_X-k8', 'LtlsX_lCfK4', 'R8y1xxxbfEg', 'ZhVFoux2EzU', 'sYsl6PqcZSs']


def recommend_videos(user_id,no_of_videos):
    rec_videos=choices(total_videos_list,k=no_of_videos)
    return rec_videos

@app.get("/")
def read_root():
    return {"Title": "HomePage Recommended Videos API","Docs":"Visit /docs for more info"}

@app.get("/videos")
async def get_rec_videos(user_id: str,no_of_videos : Union[int,None]=20):
    rec_videos=recommend_videos(user_id,no_of_videos)
    return {"user_id":user_id,"video_ids":rec_videos}
