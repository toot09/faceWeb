from simple_image_download import simple_image_download as simp
lst = ['미래통합당 증명사진','더불어민주당 증명사진','민생당 증명사진','무소속 증명사진']
for i in lst:
    response = simp.simple_image_download
    response().download(i,300)
#response = simp.simple_image_download
#response().download('무소속 증명사진',500)