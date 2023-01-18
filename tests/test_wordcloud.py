from pysentimentanalyzer.generate_wordcloud import generate_wordcloud


def test_wordcloud_valid_input():
    df = 5
    try:
        l = generate_wordcloud(df) 
        assert(False,"generate_wordcloud() should fail with input '5'")
    except:
        assert True

def test_wordcloud_valid_output_length()
    # TODO, create a df
    l = generate_wordcloud(df)
    assert(len(l) == 3, "generate_wordcloud should return 3 images")

def test_wordcloud_valid_output_type()
    # TODO, create a df
    l = generate_wordcloud(df)
    assert(isinstance(l[0],PIL.Image.Image),"generate_wordcloud() should return an image at postion 0")
    assert(isinstance(l[1],PIL.Image.Image),"generate_wordcloud() should return an image at postion 1")
    assert(isinstance(l[2],PIL.Image.Image),"generate_wordcloud() should return an image at postion 2")
    