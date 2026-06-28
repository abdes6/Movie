# ============================================================
# TMDB 模拟数据
# 当 USE_MOCK_FALLBACK=True 或 TMDB API 不可用时使用。
# 包含 20 部中英文热门电影，用于本地开发和 UI 调试。
# ============================================================

# 热门电影列表（与 TMDB /movie/popular 返回结构一致）
MOVIES_POPULAR = {
    "page": 1,
    "results": [
        {
            "id": 1, "title": "流浪地球3", "original_title": "The Wandering Earth 3",
            "overview": "太阳即将毁灭，人类在地球表面建造出巨大的推进器，寻找新的家园。",
            "poster_path": "/7pNAki9AIaJGhNFOs8ePTFI0lDc.jpg",
            "backdrop_path": "/i3GJte6Bf5sbEEVTpQQytAg8ZBE.jpg",
            "release_date": "2026-01-22", "vote_average": 8.5,
            "genre_ids": [878, 28, 12]
        },
        {
            "id": 2, "title": "哪吒之魔童闹海", "original_title": "Ne Zha 2",
            "overview": "天劫之后，哪吒和敖丙的灵魂得以保存，但肉身即将魂飞魄散。太乙真人打算用七色宝莲给二人重塑肉身。",
            "poster_path": "/bTMf8M7rZ21fChGdtsZtJj4Dfqh.jpg",
            "backdrop_path": "/3zKU2EznBtOPtheyCTQwdZL4b93.jpg",
            "release_date": "2025-01-29", "vote_average": 8.3,
            "genre_ids": [16, 14, 12]
        },
        {
            "id": 3, "title": "肖申克的救赎", "original_title": "The Shawshank Redemption",
            "overview": "银行家安迪因被误判杀害妻子及其情人而被判无期徒刑，在肖申克监狱中凭借智慧与毅力最终重获自由。",
            "poster_path": "/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
            "backdrop_path": "/zfbjgQE1uSd9wiPTX4VzsLi0rGG.jpg",
            "release_date": "1994-09-23", "vote_average": 9.3,
            "genre_ids": [18]
        },
        {
            "id": 4, "title": "千与千寻", "original_title": "Spirited Away",
            "overview": "少女千寻和父母误入一个神灵世界，为了拯救变成猪的父母，她必须在这个奇幻世界里工作并找到回家的路。",
            "poster_path": "/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
            "backdrop_path": "/dyJvKsNs2KP8qQnAXbRwDjblViy.jpg",
            "release_date": "2001-07-20", "vote_average": 8.6,
            "genre_ids": [16, 14, 10751]
        },
        {
            "id": 5, "title": "星际穿越", "original_title": "Interstellar",
            "overview": "一组探险者穿越虫洞，为人类寻找新家园的冒险故事。",
            "poster_path": "/yQvGrMoipbRoddT0ZR8tPoR7NfX.jpg",
            "backdrop_path": "/2ssWTSVklAEc98frZUQhgtGHx7s.jpg",
            "release_date": "2014-11-05", "vote_average": 8.7,
            "genre_ids": [878, 12, 18]
        },
        {
            "id": 6, "title": "让子弹飞", "original_title": "Let the Bullets Fly",
            "overview": "北洋年间，土匪张牧之劫了马邦德的花钱买官火车，冒充县长去鹅城上任，与恶霸黄四郎展开了激烈争斗。",
            "poster_path": "/pkwBO3XkQLhgb31vl5ZwmGC5meT.jpg",
            "backdrop_path": "/k1ziDzX0u8HgrAYshMb082nvtrF.jpg",
            "release_date": "2010-12-16", "vote_average": 8.8,
            "genre_ids": [28, 35, 80]
        },
        {
            "id": 7, "title": "盗梦空间", "original_title": "Inception",
            "overview": "道姆·柯布是一位经验老道的窃贼——在人们精神最为脆弱的睡梦中他能潜入别人的梦境中盗取潜意识中的秘密。",
            "poster_path": "/xlaY2zyzMfkhk0HSC5VUwzoZPU1.jpg",
            "backdrop_path": "/8ZTVqvKDQ8emSGUEMjsS4yHAwrp.jpg",
            "release_date": "2010-07-15", "vote_average": 8.8,
            "genre_ids": [28, 878, 12]
        },
        {
            "id": 8, "title": "这个杀手不太冷", "original_title": "Léon: The Professional",
            "overview": "一名职业杀手收留了一个全家被杀害的小女孩，两人之间产生了奇妙的感情。",
            "poster_path": "/wT9bYGpoFnJGiRaRF9DErVjZ7qo.jpg",
            "backdrop_path": "/qqHQsStV6exghCM7zbObuYBiYxw.jpg",
            "release_date": "1994-09-14", "vote_average": 8.5,
            "genre_ids": [28, 18, 53]
        },
        {
            "id": 9, "title": "楚门的世界", "original_title": "The Truman Show",
            "overview": "楚门是一个普通得不能再普通的人，但他不知道自己的生活其实是一档全球直播的真人秀节目。",
            "poster_path": "/vuza0WqY239yBXOadKlGwJsZJFE.jpg",
            "backdrop_path": "/aCHn2TXYJfzPXQKA6r9mKPbMlUB.jpg",
            "release_date": "1998-06-01", "vote_average": 8.4,
            "genre_ids": [35, 18]
        },
        {
            "id": 10, "title": "疯狂动物城", "original_title": "Zootopia",
            "overview": "一个现代化的动物都市，兔子朱迪通过努力实现了当警察的梦想，并与狐狸尼克搭档破获了一起大案。",
            "poster_path": "/hlK0e0wAQ3VLuJcsfIYPvb4JVud.jpg",
            "backdrop_path": "/9tOkjBEiiGcaClgJFtwocStZvIT.jpg",
            "release_date": "2016-02-11", "vote_average": 8.0,
            "genre_ids": [16, 35, 10751]
        },
        {
            "id": 11, "title": "我不是药神", "original_title": "Dying to Survive",
            "overview": "一位药店老板从印度代购白血病特效药的故事，揭示了生命与法律的冲突。",
            "poster_path": "/xxtK8DWdIwdxF5X2TJcIRDSEtE6.jpg",
            "backdrop_path": "/xNPeL9cvTCCAwlAwq7Vdq9HNJd.jpg",
            "release_date": "2018-07-05", "vote_average": 8.3,
            "genre_ids": [18, 35]
        },
        {
            "id": 12, "title": "阿甘正传", "original_title": "Forrest Gump",
            "overview": "阿甘是一个智商只有75的低能儿，但他凭借着自己的执着和善良，创造了一个又一个奇迹。",
            "poster_path": "/Cw4hIUIAmSYfK9QfaUW5igp9La.jpg",
            "backdrop_path": "/66Kn4XWhkuPkJxOJyPEx4U2CUfN.jpg",
            "release_date": "1994-06-23", "vote_average": 8.8,
            "genre_ids": [35, 18, 10749]
        },
        {
            "id": 13, "title": "釜山行", "original_title": "Train to Busan",
            "overview": "一列从首尔开往釜山的高速列车上，突然爆发丧尸病毒，乘客们在封闭的空间中为生存而战。",
            "poster_path": "/vNVFt6dtcqnI7hqa6LFBUibuFiw.jpg",
            "backdrop_path": "/qFKb25O9ROiGYt3GwtuXG5Lb2J.jpg",
            "release_date": "2016-07-20", "vote_average": 7.6,
            "genre_ids": [27, 28, 53]
        },
        {
            "id": 14, "title": "怦然心动", "original_title": "Flipped",
            "overview": "朱莉安娜·贝克对搬来的邻居男孩布莱斯一见钟情，两人之间发生了纯真美好的青春故事。",
            "poster_path": "/6zDYFigohwncqFL00MKbFV01dWb.jpg",
            "backdrop_path": "/xBSwwkAYl9h8QVG2OxNpSaSgJwr.jpg",
            "release_date": "2010-07-26", "vote_average": 8.2,
            "genre_ids": [35, 10749]
        },
        {
            "id": 15, "title": "海上钢琴师", "original_title": "The Legend of 1900",
            "overview": "一个在邮轮上长大的钢琴天才，一生从未踏足陆地，与音乐相伴的传奇人生。",
            "poster_path": "/iOcbJ5pxokOPDRgieVDbsFMrCc6.jpg",
            "backdrop_path": "/muSeX7fnNw0pv4zHK7RSwZln6Hk.jpg",
            "release_date": "1998-10-28", "vote_average": 8.6,
            "genre_ids": [18, 10402]
        },
        {
            "id": 16, "title": "唐探1900", "original_title": "Detective Chinatown 1900",
            "overview": "1900年的旧金山，唐人街发生了一起神秘谋杀案，留学生和当地侦探联手破案。",
            "poster_path": "/g3GsgIlH3fA4RxhNOAMvSbVWyfW.jpg",
            "backdrop_path": "/4xN3phAX024b251CPhy8zvsXbBc.jpg",
            "release_date": "2025-01-29", "vote_average": 7.0,
            "genre_ids": [35, 9648, 80]
        },
        {
            "id": 17, "title": "寻梦环游记", "original_title": "Coco",
            "overview": "热爱音乐的小男孩米格在亡灵节误入亡灵世界，与已故曾曾祖父一起踏上了寻找音乐梦想的旅程。",
            "poster_path": "/6Ryitt95xrO8KXuqRGm1fUuNwqF.jpg",
            "backdrop_path": "/g7CHF8gTLGooTbP4GznIGwaqAGL.jpg",
            "release_date": "2017-10-27", "vote_average": 8.4,
            "genre_ids": [16, 14, 10751]
        },
        {
            "id": 18, "title": "霸王别姬", "original_title": "Farewell My Concubine",
            "overview": "段小楼与程蝶衣从小在戏班学艺，两人合演《霸王别姬》誉满京城。横跨半个世纪的悲欢离合。",
            "poster_path": "/f54hNIiHNINw3JiUJB2XaQl5wCN.jpg",
            "backdrop_path": "/bBiZN1epQTu3F8iFLBuMhc4TRzr.jpg",
            "release_date": "1993-01-01", "vote_average": 9.6,
            "genre_ids": [18, 10749, 36]
        },
        {
            "id": 19, "title": "泰勒·斯威夫特：时代巡回演唱会",
            "original_title": "Taylor Swift: The Eras Tour",
            "overview": "泰勒·斯威夫特破纪录的时代巡回演唱会在大银幕上精彩呈现。",
            "poster_path": "/jf3YO8hOqGHCupsREf5qymYq1n.jpg",
            "backdrop_path": "/wVJG3u5Ru9tInxYiTCrJr4MpJ7Z.jpg",
            "release_date": "2023-10-13", "vote_average": 8.3,
            "genre_ids": [10402, 99]
        },
        {
            "id": 20, "title": "奥本海默", "original_title": "Oppenheimer",
            "overview": "讲述了美国\"原子弹之父\"罗伯特·奥本海默的故事，以及他在二战期间领导曼哈顿计划的历史。",
            "poster_path": "/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
            "backdrop_path": "/neeNHeXjMF5fXoCJRsOmkNGC7q.jpg",
            "release_date": "2023-07-19", "vote_average": 8.5,
            "genre_ids": [18, 36]
        }
    ],
    "total_pages": 1,
    "total_results": 20
}

# 高分电影列表（与 TMDB /movie/top_rated 结构一致）
MOVIES_TOP_RATED = {
    "page": 1,
    "results": [
        {
            "id": 18, "title": "霸王别姬", "original_title": "Farewell My Concubine",
            "overview": "段小楼与程蝶衣从小在戏班学艺，两人合演《霸王别姬》誉满京城。",
            "poster_path": "/f54hNIiHNINw3JiUJB2XaQl5wCN.jpg",
            "backdrop_path": "/bBiZN1epQTu3F8iFLBuMhc4TRzr.jpg",
            "release_date": "1993-01-01", "vote_average": 9.6,
            "genre_ids": [18, 10749, 36]
        },
        {
            "id": 3, "title": "肖申克的救赎", "original_title": "The Shawshank Redemption",
            "overview": "银行家安迪因被误判杀害妻子及其情人而被判无期徒刑，在肖申克监狱中凭借智慧与毅力最终重获自由。",
            "poster_path": "/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
            "backdrop_path": "/zfbjgQE1uSd9wiPTX4VzsLi0rGG.jpg",
            "release_date": "1994-09-23", "vote_average": 9.3,
            "genre_ids": [18]
        },
        {
            "id": 6, "title": "让子弹飞", "original_title": "Let the Bullets Fly",
            "overview": "北洋年间，土匪张牧之劫了马邦德的花钱买官火车。",
            "poster_path": "/pkwBO3XkQLhgb31vl5ZwmGC5meT.jpg",
            "backdrop_path": "/k1ziDzX0u8HgrAYshMb082nvtrF.jpg",
            "release_date": "2010-12-16", "vote_average": 8.8,
            "genre_ids": [28, 35, 80]
        },
        {
            "id": 7, "title": "盗梦空间", "original_title": "Inception",
            "overview": "道姆·柯布在人们睡梦中潜入别人梦境盗取潜意识中的秘密。",
            "poster_path": "/xlaY2zyzMfkhk0HSC5VUwzoZPU1.jpg",
            "backdrop_path": "/8ZTVqvKDQ8emSGUEMjsS4yHAwrp.jpg",
            "release_date": "2010-07-15", "vote_average": 8.8,
            "genre_ids": [28, 878, 12]
        },
        {
            "id": 12, "title": "阿甘正传", "original_title": "Forrest Gump",
            "overview": "阿甘智商只有75，但凭借执着和善良创造了一个又一个奇迹。",
            "poster_path": "/Cw4hIUIAmSYfK9QfaUW5igp9La.jpg",
            "backdrop_path": "/66Kn4XWhkuPkJxOJyPEx4U2CUfN.jpg",
            "release_date": "1994-06-23", "vote_average": 8.8,
            "genre_ids": [35, 18, 10749]
        },
        {
            "id": 5, "title": "星际穿越", "original_title": "Interstellar",
            "overview": "一组探险者穿越虫洞为人类寻找新家园的冒险故事。",
            "poster_path": "/yQvGrMoipbRoddT0ZR8tPoR7NfX.jpg",
            "backdrop_path": "/2ssWTSVklAEc98frZUQhgtGHx7s.jpg",
            "release_date": "2014-11-05", "vote_average": 8.7,
            "genre_ids": [878, 12, 18]
        },
        {
            "id": 4, "title": "千与千寻", "original_title": "Spirited Away",
            "overview": "少女千寻误入神灵世界，为了拯救变成猪的父母而在这个世界工作。",
            "poster_path": "/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
            "backdrop_path": "/dyJvKsNs2KP8qQnAXbRwDjblViy.jpg",
            "release_date": "2001-07-20", "vote_average": 8.6,
            "genre_ids": [16, 14, 10751]
        },
        {
            "id": 15, "title": "海上钢琴师", "original_title": "The Legend of 1900",
            "overview": "一个在邮轮上长大的钢琴天才，与音乐相伴的传奇人生。",
            "poster_path": "/iOcbJ5pxokOPDRgieVDbsFMrCc6.jpg",
            "backdrop_path": "/muSeX7fnNw0pv4zHK7RSwZln6Hk.jpg",
            "release_date": "1998-10-28", "vote_average": 8.6,
            "genre_ids": [18, 10402]
        },
        {
            "id": 1, "title": "流浪地球3", "original_title": "The Wandering Earth 3",
            "overview": "太阳即将毁灭，人类在地球表面建造出巨大的推进器，寻找新的家园。",
            "poster_path": "/twdgFrp9Sd8rb3TdbWFQXAvslrH.jpg",
            "backdrop_path": "/i3GJte6Bf5sbEEVTpQQytAg8ZBE.jpg",
            "release_date": "2026-01-22", "vote_average": 8.5,
            "genre_ids": [878, 28, 12]
        },
        {
            "id": 8, "title": "这个杀手不太冷", "original_title": "Léon: The Professional",
            "overview": "一名职业杀手收留了一个全家被杀害的小女孩。",
            "poster_path": "/wT9bYGpoFnJGiRaRF9DErVjZ7qo.jpg",
            "backdrop_path": "/qqHQsStV6exghCM7zbObuYBiYxw.jpg",
            "release_date": "1994-09-14", "vote_average": 8.5,
            "genre_ids": [28, 18, 53]
        },
        {
            "id": 20, "title": "奥本海默", "original_title": "Oppenheimer",
            "overview": "讲述了美国原子弹之父罗伯特·奥本海默的故事。",
            "poster_path": "/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
            "backdrop_path": "/neeNHeXjMF5fXoCJRsOmkNGC7q.jpg",
            "release_date": "2023-07-19", "vote_average": 8.5,
            "genre_ids": [18, 36]
        },
        {
            "id": 9, "title": "楚门的世界", "original_title": "The Truman Show",
            "overview": "楚门的生活其实是一档全球直播的真人秀节目。",
            "poster_path": "/vuza0WqY239yBXOadKlGwJsZJFE.jpg",
            "backdrop_path": "/aCHn2TXYJfzPXQKA6r9mKPbMlUB.jpg",
            "release_date": "1998-06-01", "vote_average": 8.4,
            "genre_ids": [35, 18]
        },
        {
            "id": 17, "title": "寻梦环游记", "original_title": "Coco",
            "overview": "热爱音乐的小男孩米格在亡灵节误入亡灵世界。",
            "poster_path": "/6Ryitt95xrO8KXuqRGm1fUuNwqF.jpg",
            "backdrop_path": "/g7CHF8gTLGooTbP4GznIGwaqAGL.jpg",
            "release_date": "2017-10-27", "vote_average": 8.4,
            "genre_ids": [16, 14, 10751]
        },
        {
            "id": 2, "title": "哪吒之魔童闹海", "original_title": "Ne Zha 2",
            "overview": "天劫之后哪吒和敖丙灵魂得以保存，太乙真人用七色宝莲重塑肉身。",
            "poster_path": "/bTMf8M7rZ21fChGdtsZtJj4Dfqh.jpg",
            "backdrop_path": "/3zKU2EznBtOPtheyCTQwdZL4b93.jpg",
            "release_date": "2025-01-29", "vote_average": 8.3,
            "genre_ids": [16, 14, 12]
        },
        {
            "id": 11, "title": "我不是药神", "original_title": "Dying to Survive",
            "overview": "一位药店老板从印度代购白血病特效药的故事。",
            "poster_path": "/xxtK8DWdIwdxF5X2TJcIRDSEtE6.jpg",
            "backdrop_path": "/xNPeL9cvTCCAwlAwq7Vdq9HNJd.jpg",
            "release_date": "2018-07-05", "vote_average": 8.3,
            "genre_ids": [18, 35]
        },
        {
            "id": 14, "title": "怦然心动", "original_title": "Flipped",
            "overview": "朱莉安娜对搬来的邻居男孩布莱斯一见钟情的青春故事。",
            "poster_path": "/6zDYFigohwncqFL00MKbFV01dWb.jpg",
            "backdrop_path": "/xBSwwkAYl9h8QVG2OxNpSaSgJwr.jpg",
            "release_date": "2010-07-26", "vote_average": 8.2,
            "genre_ids": [35, 10749]
        },
        {
            "id": 10, "title": "疯狂动物城", "original_title": "Zootopia",
            "overview": "兔子朱迪通过努力实现警察梦想，与狐狸尼克搭档破获大案。",
            "poster_path": "/hlK0e0wAQ3VLuJcsfIYPvb4JVud.jpg",
            "backdrop_path": "/9tOkjBEiiGcaClgJFtwocStZvIT.jpg",
            "release_date": "2016-02-11", "vote_average": 8.0,
            "genre_ids": [16, 35, 10751]
        },
        {
            "id": 13, "title": "釜山行", "original_title": "Train to Busan",
            "overview": "一列从首尔开往釜山的列车上突然爆发丧尸病毒。",
            "poster_path": "/vNVFt6dtcqnI7hqa6LFBUibuFiw.jpg",
            "backdrop_path": "/qFKb25O9ROiGYt3GwtuXG5Lb2J.jpg",
            "release_date": "2016-07-20", "vote_average": 7.6,
            "genre_ids": [27, 28, 53]
        },
        {
            "id": 16, "title": "唐探1900", "original_title": "Detective Chinatown 1900",
            "overview": "1900年旧金山唐人街一起神秘谋杀案。",
            "poster_path": "/g3GsgIlH3fA4RxhNOAMvSbVWyfW.jpg",
            "backdrop_path": "/4xN3phAX024b251CPhy8zvsXbBc.jpg",
            "release_date": "2025-01-29", "vote_average": 7.0,
            "genre_ids": [35, 9648, 80]
        }
    ],
    "total_pages": 1,
    "total_results": 19
}

# 正在上映电影列表（与 TMDB /movie/now_playing 结构一致）
MOVIES_NOW_PLAYING = {
    "page": 1,
    "results": [
        {
            "id": 1, "title": "流浪地球3", "original_title": "The Wandering Earth 3",
            "overview": "太阳即将毁灭，人类在地球表面建造出巨大的推进器。",
            "poster_path": "w1280/7pNAki9AIaJGhNFOs8ePTFI0lDc.jpg",
            "backdrop_path": "/i3GJte6Bf5sbEEVTpQQytAg8ZBE.jpg",
            "release_date": "2026-01-22", "vote_average": 8.5,
            "genre_ids": [878, 28, 12]
        },
        {
            "id": 16, "title": "唐探1900", "original_title": "Detective Chinatown 1900",
            "overview": "1900年旧金山唐人街一起神秘谋杀案。",
            "poster_path": "/g3GsgIlH3fA4RxhNOAMvSbVWyfW.jpg",
            "backdrop_path": "/4xN3phAX024b251CPhy8zvsXbBc.jpg",
            "release_date": "2025-01-29", "vote_average": 7.0,
            "genre_ids": [35, 9648, 80]
        },
        {
            "id": 19, "title": "泰勒·斯威夫特：时代巡回演唱会",
            "original_title": "Taylor Swift: The Eras Tour",
            "overview": "泰勒·斯威夫特破纪录的时代巡回演唱会。",
            "poster_path": "/jf3YO8hOqGHCupsREf5qymYq1n.jpg",
            "backdrop_path": "/wVJG3u5Ru9tInxYiTCrJr4MpJ7Z.jpg",
            "release_date": "2023-10-13", "vote_average": 8.3,
            "genre_ids": [10402, 99]
        },
        {
            "id": 2, "title": "哪吒之魔童闹海", "original_title": "Ne Zha 2",
            "overview": "天劫之后哪吒和敖丙灵魂得以保存。",
            "poster_path": "/bTMf8M7rZ21fChGdtsZtJj4Dfqh.jpg",
            "backdrop_path": "/3zKU2EznBtOPtheyCTQwdZL4b93.jpg",
            "release_date": "2025-01-29", "vote_average": 8.3,
            "genre_ids": [16, 14, 12]
        }
    ],
    "total_pages": 1,
    "total_results": 4
}

# 电影详情字典（与 TMDB /movie/{id}?append_to_response=credits,recommendations 结构一致）
# 键为电影 ID，值为包含 cast/director/recommendations 的完整详情
MOVIE_DETAILS: dict = {
    1: {
        "id": 1, "title": "流浪地球3", "original_title": "The Wandering Earth 3",
        "overview": "太阳即将毁灭，人类在地球表面建造出巨大的推进器，寻找新的家园。面对前所未有的危机，各国宇航员挺身而出，携手展开一场关乎人类命运的太空救援行动。",
        "poster_path": "/7pNAki9AIaJGhNFOs8ePTFI0lDc.jpg",
        "backdrop_path": "/i3GJte6Bf5sbEEVTpQQytAg8ZBE.jpg",
        "release_date": "2026-01-22", "vote_average": 8.5,
        "genre_ids": [878, 28, 12],
        "runtime": 145,
        "director": "郭帆",
        "cast": [
            {"name": "吴京", "character": "刘培强", "profile_path": "/cFuATO6PnffJXtsYF7BRqhCXlwe.jpg"},
            {"name": "刘德华", "character": "图恒宇", "profile_path": "/z9R2yerjfgxwDWIH8sjiS0hhcre.jpg"},
            {"name": "李雪健", "character": "周喆直", "profile_path": "/22QFJKWJPNj3O3A6PdRKJc0qeKK.jpg"}
        ],
        "recommendations": [
            {"id": 5, "title": "星际穿越", "original_title": "Interstellar",
             "overview": "穿越虫洞为人类寻找新家园。", "poster_path": "/yQvGrMoipbRoddT0ZR8tPoR7NfX.jpg",
             "backdrop_path": "/2ssWTSVklAEc98frZUQhgtGHx7s.jpg", "release_date": "2014-11-05",
             "vote_average": 8.7, "genre_ids": [878, 12, 18]},
            {"id": 7, "title": "盗梦空间", "original_title": "Inception",
             "overview": "潜入梦境盗取秘密。", "poster_path": "/xlaY2zyzMfkhk0HSC5VUwzoZPU1.jpg",
             "backdrop_path": "/8ZTVqvKDQ8emSGUEMjsS4yHAwrp.jpg", "release_date": "2010-07-15",
             "vote_average": 8.8, "genre_ids": [28, 878, 12]}
        ]
    },
    2: {
        "id": 2, "title": "哪吒之魔童闹海", "original_title": "Ne Zha 2",
        "overview": "天劫之后，哪吒和敖丙的灵魂得以保存，但肉身即将魂飞魄散。太乙真人打算用七色宝莲给二人重塑肉身。然而在重塑肉身的过程中遇到重重困难，哪吒和敖丙的命运将走向何方？",
        "poster_path": "/bTMf8M7rZ21fChGdtsZtJj4Dfqh.jpg",
        "backdrop_path": "/bTMf8M7rZ21fChGdtsZtJj4Dfqh.jpg",
        "release_date": "2025-01-29", "vote_average": 8.3,
        "genre_ids": [16, 14, 12],
        "runtime": 144,
        "director": "饺子",
        "cast": [
            {"name": "吕艳婷", "character": "哪吒（配音）", "profile_path": "/vKpOzPutTaPf03rWXiLuK8R2K3B.jpg"},
            {"name": "囧森瑟夫", "character": "敖丙（配音）", "profile_path": "/1TgCL0mlekWivRNo1voCwUZ8I5s.jpg"}
        ],
        "recommendations": [
            {"id": 17, "title": "寻梦环游记", "original_title": "Coco",
             "overview": "亡灵节的奇幻冒险。", "poster_path": "/6Ryitt95xrO8KXuqRGm1fUuNwqF.jpg",
             "backdrop_path": "/g7CHF8gTLGooTbP4GznIGwaqAGL.jpg", "release_date": "2017-10-27",
             "vote_average": 8.4, "genre_ids": [16, 14, 10751]},
            {"id": 10, "title": "疯狂动物城", "original_title": "Zootopia",
             "overview": "动物都市的警察梦。", "poster_path": "/hlK0e0wAQ3VLuJcsfIYPvb4JVud.jpg",
             "backdrop_path": "/9tOkjBEiiGcaClgJFtwocStZvIT.jpg", "release_date": "2016-02-11",
             "vote_average": 8.0, "genre_ids": [16, 35, 10751]}
        ]
    },
    3: {
        "id": 3, "title": "肖申克的救赎", "original_title": "The Shawshank Redemption",
        "overview": "银行家安迪·杜弗雷因被误判杀害妻子及其情人而被判无期徒刑，关押在肖申克监狱。在监狱中他结识了囚犯瑞德，凭借自己的金融知识和坚韧的毅力，在20年的时间里最终成功越狱并揭露了监狱长的腐败。",
        "poster_path": "/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
        "backdrop_path": "/zfbjgQE1uSd9wiPTX4VzsLi0rGG.jpg",
        "release_date": "1994-09-23", "vote_average": 9.3,
        "genre_ids": [18],
        "runtime": 142,
        "director": "弗兰克·德拉邦特",
        "cast": [
            {"name": "蒂姆·罗宾斯", "character": "安迪·杜弗雷", "profile_path": "/3FfJMIVwXgsIXbAT8ECBSZJAncR.jpg"},
            {"name": "摩根·弗里曼", "character": "埃利斯·瑞德", "profile_path": "/1ahENoyEgKSbRUd0IsydIff7rt1.jpg"}
        ],
        "recommendations": [
            {"id": 12, "title": "阿甘正传", "original_title": "Forrest Gump",
             "overview": "一个低能儿创造的奇迹。", "poster_path": "/Cw4hIUIAmSYfK9QfaUW5igp9La.jpg",
             "backdrop_path": "/66Kn4XWhkuPkJxOJyPEx4U2CUfN.jpg", "release_date": "1994-06-23",
             "vote_average": 8.8, "genre_ids": [35, 18, 10749]},
            {"id": 9, "title": "楚门的世界", "original_title": "The Truman Show",
             "overview": "全球直播的真人秀。", "poster_path": "/vuza0WqY239yBXOadKlGwJsZJFE.jpg",
             "backdrop_path": "/aCHn2TXYJfzPXQKA6r9mKPbMlUB.jpg", "release_date": "1998-06-01",
             "vote_average": 8.4, "genre_ids": [35, 18]}
        ]
    },
    4: {
        "id": 4, "title": "千与千寻", "original_title": "Spirited Away",
        "overview": "少女千寻和父母误入一个神灵世界。父母因贪吃变成了猪，千寻为了拯救父母，在神秘少年白龙的帮助下，在汤婆婆的浴场工作。她经历了各种奇幻冒险，最终找到了回家的路。",
        "poster_path": "/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
        "backdrop_path": "/dyJvKsNs2KP8qQnAXbRwDjblViy.jpg",
        "release_date": "2001-07-20", "vote_average": 8.6,
        "genre_ids": [16, 14, 10751],
        "runtime": 125,
        "director": "宫崎骏",
        "cast": [
            {"name": "柊瑠美", "character": "千寻（配音）", "profile_path": None},
            {"name": "入野自由", "character": "白龙（配音）", "profile_path": "/8qEEhHUObNvGQr4e6eqLu5z4qTz.jpg"}
        ],
        "recommendations": [
            {"id": 17, "title": "寻梦环游记", "original_title": "Coco",
             "overview": "亡灵节的奇幻冒险。", "poster_path": "/6Ryitt95xrO8KXuqRGm1fUuNwqF.jpg",
             "backdrop_path": "/g7CHF8gTLGooTbP4GznIGwaqAGL.jpg", "release_date": "2017-10-27",
             "vote_average": 8.4, "genre_ids": [16, 14, 10751]},
            {"id": 10, "title": "疯狂动物城", "original_title": "Zootopia",
             "overview": "动物都市的警察梦。", "poster_path": "/hlK0e0wAQ3VLuJcsfIYPvb4JVud.jpg",
             "backdrop_path": "/9tOkjBEiiGcaClgJFtwocStZvIT.jpg", "release_date": "2016-02-11",
             "vote_average": 8.0, "genre_ids": [16, 35, 10751]}
        ]
    },
    5: {
        "id": 5, "title": "星际穿越", "original_title": "Interstellar",
        "overview": "在不久的将来，地球面临着严重的粮食危机和沙尘暴。前NASA宇航员库珀被选中参与一项穿越虫洞的星际旅行，为人类寻找新的家园。在浩瀚的宇宙中，他们发现了时间膨胀的惊人效应，也面临着艰难的选择。",
        "poster_path": "/yQvGrMoipbRoddT0ZR8tPoR7NfX.jpg",
        "backdrop_path": "/2ssWTSVklAEc98frZUQhgtGHx7s.jpg",
        "release_date": "2014-11-05", "vote_average": 8.7,
        "genre_ids": [878, 12, 18],
        "runtime": 169,
        "director": "克里斯托弗·诺兰",
        "cast": [
            {"name": "马修·麦康纳", "character": "库珀", "profile_path": "/lCySuYjhXix3FzQdS4oceDDrXKI.jpg"},
            {"name": "安妮·海瑟薇", "character": "布兰德", "profile_path": "/nbccV2pMoyLTCeg5DQip24Eq0Jp.jpg"},
            {"name": "杰西卡·查斯坦", "character": "墨菲", "profile_path": "/eQKnihReJeB9vQEa5gySzAlKfZt.jpg"}
        ],
        "recommendations": [
            {"id": 1, "title": "流浪地球3", "original_title": "The Wandering Earth 3",
             "overview": "人类寻找新家园。", "poster_path": "/7pNAki9AIaJGhNFOs8ePTFI0lDc.jpg",
             "backdrop_path": "/7pNAki9AIaJGhNFOs8ePTFI0lDc.jpg", "release_date": "2026-01-22",
             "vote_average": 8.5, "genre_ids": [878, 28, 12]},
            {"id": 7, "title": "盗梦空间", "original_title": "Inception",
             "overview": "潜入梦境盗取秘密。", "poster_path": "/xlaY2zyzMfkhk0HSC5VUwzoZPU1.jpg",
             "backdrop_path": "/8ZTVqvKDQ8emSGUEMjsS4yHAwrp.jpg", "release_date": "2010-07-15",
             "vote_average": 8.8, "genre_ids": [28, 878, 12]}
        ]
    },
    6: {
        "id": 6, "title": "让子弹飞", "original_title": "Let the Bullets Fly",
        "overview": "北洋年间，土匪张牧之劫了马邦德的花钱买官火车，冒充县长去鹅城上任。鹅城恶霸黄四郎只手遮天，张牧之与黄四郎之间的智斗与枪战一触即发，在这场充满黑色幽默的较量中，每个人都在为各自的信念而战。",
        "poster_path": "/pkwBO3XkQLhgb31vl5ZwmGC5meT.jpg",
        "backdrop_path": "/k1ziDzX0u8HgrAYshMb082nvtrF.jpg",
        "release_date": "2010-12-16", "vote_average": 8.8,
        "genre_ids": [28, 35, 80],
        "runtime": 132,
        "director": "姜文",
        "cast": [
            {"name": "姜文", "character": "张牧之", "profile_path": None},
            {"name": "周润发", "character": "黄四郎", "profile_path": "/2Jybmz4PSuilsSnmQ4tYWXykPjC.jpg"},
            {"name": "葛优", "character": "马邦德", "profile_path": None}
        ],
        "recommendations": [
            {"id": 7, "title": "盗梦空间", "original_title": "Inception",
             "overview": "潜入梦境盗取秘密。", "poster_path": "/xlaY2zyzMfkhk0HSC5VUwzoZPU1.jpg",
             "backdrop_path": "/8ZTVqvKDQ8emSGUEMjsS4yHAwrp.jpg", "release_date": "2010-07-15",
             "vote_average": 8.8, "genre_ids": [28, 878, 12]},
            {"id": 8, "title": "这个杀手不太冷", "original_title": "Léon: The Professional",
             "overview": "职业杀手与小女孩的温情故事。", "poster_path": "/wT9bYGpoFnJGiRaRF9DErVjZ7qo.jpg",
             "backdrop_path": "/qqHQsStV6exghCM7zbObuYBiYxw.jpg", "release_date": "1994-09-14",
             "vote_average": 8.5, "genre_ids": [28, 18, 53]}
        ]
    },
    7: {
        "id": 7, "title": "盗梦空间", "original_title": "Inception",
        "overview": "道姆·柯布是一位经验老道的窃贼——在人们精神最为脆弱的睡梦中他能潜入别人的梦境中盗取潜意识中的秘密。为了回到孩子身边，他接受了一个看似不可能的任务：在目标人物的潜意识中植入一个想法。在多重梦境中，现实与梦境的边界逐渐模糊。",
        "poster_path": "/xlaY2zyzMfkhk0HSC5VUwzoZPU1.jpg",
        "backdrop_path": "/8ZTVqvKDQ8emSGUEMjsS4yHAwrp.jpg",
        "release_date": "2010-07-15", "vote_average": 8.8,
        "genre_ids": [28, 878, 12],
        "runtime": 148,
        "director": "克里斯托弗·诺兰",
        "cast": [
            {"name": "莱昂纳多·迪卡普里奥", "character": "道姆·柯布", "profile_path": "/mkdRcVIQl4WZhDf1vXKWTD7HZrZ.jpg"},
            {"name": "渡边谦", "character": "斋藤", "profile_path": "/psAXOYp9SBOXvg6AXzARDedNQ9P.jpg"},
            {"name": "玛丽昂·歌迪亚", "character": "梅尔", "profile_path": "/l4nlpTeRqdihBQisr0VG0eIF719.jpg"}
        ],
        "recommendations": [
            {"id": 5, "title": "星际穿越", "original_title": "Interstellar",
             "overview": "穿越虫洞为人类寻找新家园。", "poster_path": "/yQvGrMoipbRoddT0ZR8tPoR7NfX.jpg",
             "backdrop_path": "/2ssWTSVklAEc98frZUQhgtGHx7s.jpg", "release_date": "2014-11-05",
             "vote_average": 8.7, "genre_ids": [878, 12, 18]},
            {"id": 1, "title": "流浪地球3", "original_title": "The Wandering Earth 3",
             "overview": "人类寻找新家园。", "poster_path": "/twdgFrp9Sd8rb3TdbWFQXAvslrH.jpg",
             "backdrop_path": "/i3GJte6Bf5sbEEVTpQQytAg8ZBE.jpg", "release_date": "2026-01-22",
             "vote_average": 8.5, "genre_ids": [878, 28, 12]}
        ]
    },
    8: {
        "id": 8, "title": "这个杀手不太冷", "original_title": "Léon: The Professional",
        "overview": "纽约贫民区住着一个沉默寡言的职业杀手莱昂，他独来独往，技艺精湛。邻居家小女孩玛蒂尔达因全家被缉毒警察杀害而闯入了他的生活。两个孤独的灵魂在相处中建立了奇妙的感情，莱昂冰冷的心逐渐被融化。",
        "poster_path": "/wT9bYGpoFnJGiRaRF9DErVjZ7qo.jpg",
        "backdrop_path": "/qqHQsStV6exghCM7zbObuYBiYxw.jpg",
        "release_date": "1994-09-14", "vote_average": 8.5,
        "genre_ids": [28, 18, 53],
        "runtime": 133,
        "director": "吕克·贝松",
        "cast": [
            {"name": "让·雷诺", "character": "莱昂", "profile_path": "/mw0EZJYz3kiFq9fNxsML773gotF.jpg"},
            {"name": "娜塔莉·波特曼", "character": "玛蒂尔达", "profile_path": "/edPU5HxncLWa1YkgRPNkSd68ONG.jpg"}
        ],
        "recommendations": [
            {"id": 7, "title": "盗梦空间", "original_title": "Inception",
             "overview": "潜入梦境盗取秘密。", "poster_path": "/xlaY2zyzMfkhk0HSC5VUwzoZPU1.jpg",
             "backdrop_path": "/8ZTVqvKDQ8emSGUEMjsS4yHAwrp.jpg", "release_date": "2010-07-15",
             "vote_average": 8.8, "genre_ids": [28, 878, 12]},
            {"id": 6, "title": "让子弹飞", "original_title": "Let the Bullets Fly",
             "overview": "土匪与恶霸的智斗。", "poster_path": "/pkwBO3XkQLhgb31vl5ZwmGC5meT.jpg",
             "backdrop_path": "/k1ziDzX0u8HgrAYshMb082nvtrF.jpg", "release_date": "2010-12-16",
             "vote_average": 8.8, "genre_ids": [28, 35, 80]}
        ]
    },
    9: {
        "id": 9, "title": "楚门的世界", "original_title": "The Truman Show",
        "overview": "楚门是一个普通得不能再普通的人，但他的人生从出生起就被安排成了一档全球直播的真人秀节目。他所居住的海景镇是一个巨大的摄影棚，身边的亲人朋友都是演员。当楚门逐渐发现真相，他决定不惜一切代价走出这个虚假的世界。",
        "poster_path": "/vuza0WqY239yBXOadKlGwJsZJFE.jpg",
        "backdrop_path": "/aCHn2TXYJfzPXQKA6r9mKPbMlUB.jpg",
        "release_date": "1998-06-01", "vote_average": 8.4,
        "genre_ids": [35, 18],
        "runtime": 103,
        "director": "彼得·威尔",
        "cast": [
            {"name": "金·凯瑞", "character": "楚门·伯班克", "profile_path": "/y3U9QfPN6sJaGl6l68xjwWj28ig.jpg"},
            {"name": "劳拉·琳妮", "character": "美露", "profile_path": "/yIopIq7l7eIvjoQqnZJkpdQEvds.jpg"}
        ],
        "recommendations": [
            {"id": 12, "title": "阿甘正传", "original_title": "Forrest Gump",
             "overview": "一个低能儿创造的奇迹。", "poster_path": "/Cw4hIUIAmSYfK9QfaUW5igp9La.jpg",
             "backdrop_path": "/66Kn4XWhkuPkJxOJyPEx4U2CUfN.jpg", "release_date": "1994-06-23",
             "vote_average": 8.8, "genre_ids": [35, 18, 10749]},
            {"id": 14, "title": "怦然心动", "original_title": "Flipped",
             "overview": "纯真美好的青春故事。", "poster_path": "/6zDYFigohwncqFL00MKbFV01dWb.jpg",
             "backdrop_path": "/xBSwwkAYl9h8QVG2OxNpSaSgJwr.jpg", "release_date": "2010-07-26",
             "vote_average": 8.2, "genre_ids": [35, 10749]}
        ]
    },
    10: {
        "id": 10, "title": "疯狂动物城", "original_title": "Zootopia",
        "overview": "一个现代化的动物都市，各种动物在这里和平共处。兔子朱迪从小就梦想成为一名警察，尽管受到嘲笑，她凭借努力终于实现了梦想。为了证明自己，她与狐狸尼克搭档破获了一桩动物失踪案，却意外揭开了一个惊天阴谋。",
        "poster_path": "/hlK0e0wAQ3VLuJcsfIYPvb4JVud.jpg",
        "backdrop_path": "/9tOkjBEiiGcaClgJFtwocStZvIT.jpg",
        "release_date": "2016-02-11", "vote_average": 8.0,
        "genre_ids": [16, 35, 10751],
        "runtime": 108,
        "director": "拜伦·霍华德",
        "cast": [
            {"name": "金妮弗·古德温", "character": "朱迪·霍普斯（配音）", "profile_path": "/n8XOnjgyfYvqRUDcnkAckRqSaNN.jpg"},
            {"name": "杰森·贝特曼", "character": "尼克·王尔德（配音）", "profile_path": "/wS22fofYtUf4aGXACFwhkTjUk6a.jpg"}
        ],
        "recommendations": [
            {"id": 17, "title": "寻梦环游记", "original_title": "Coco",
             "overview": "亡灵节的奇幻冒险。", "poster_path": "/6Ryitt95xrO8KXuqRGm1fUuNwqF.jpg",
             "backdrop_path": "/g7CHF8gTLGooTbP4GznIGwaqAGL.jpg", "release_date": "2017-10-27",
             "vote_average": 8.4, "genre_ids": [16, 14, 10751]},
            {"id": 4, "title": "千与千寻", "original_title": "Spirited Away",
             "overview": "少女在神灵世界的奇幻冒险。", "poster_path": "/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
             "backdrop_path": "/dyJvKsNs2KP8qQnAXbRwDjblViy.jpg", "release_date": "2001-07-20",
             "vote_average": 8.6, "genre_ids": [16, 14, 10751]}
        ]
    },
    11: {
        "id": 11, "title": "我不是药神", "original_title": "Dying to Survive",
        "overview": "一位保健品店老板程勇因生活窘迫，在白血病患者的恳求下，从印度走私廉价的仿制抗癌药。这种药疗效与正版药无异，但价格只有十分之一。程勇在金钱与道义之间挣扎，最终走上了一条救人于水火的不归路。",
        "poster_path": "/xxtK8DWdIwdxF5X2TJcIRDSEtE6.jpg",
        "backdrop_path": "/xNPeL9cvTCCAwlAwq7Vdq9HNJd.jpg",
        "release_date": "2018-07-05", "vote_average": 8.3,
        "genre_ids": [18, 35],
        "runtime": 117,
        "director": "文牧野",
        "cast": [
            {"name": "徐峥", "character": "程勇", "profile_path": "/yclQtqxPnlp7H4seiKltNfJjlrc.jpg"},
            {"name": "王传君", "character": "吕受益", "profile_path": "/ilFW1ONI5UILya7nC1SuqZtkGRG.jpg"}
        ],
        "recommendations": [
            {"id": 12, "title": "阿甘正传", "original_title": "Forrest Gump",
             "overview": "一个低能儿创造的奇迹。", "poster_path": "/Cw4hIUIAmSYfK9QfaUW5igp9La.jpg",
             "backdrop_path": "/66Kn4XWhkuPkJxOJyPEx4U2CUfN.jpg", "release_date": "1994-06-23",
             "vote_average": 8.8, "genre_ids": [35, 18, 10749]},
            {"id": 9, "title": "楚门的世界", "original_title": "The Truman Show",
             "overview": "全球直播的真人秀。", "poster_path": "/vuza0WqY239yBXOadKlGwJsZJFE.jpg",
             "backdrop_path": "/aCHn2TXYJfzPXQKA6r9mKPbMlUB.jpg", "release_date": "1998-06-01",
             "vote_average": 8.4, "genre_ids": [35, 18]}
        ]
    },
    12: {
        "id": 12, "title": "阿甘正传", "original_title": "Forrest Gump",
        "overview": "阿甘是一个智商仅75的善良青年，但他的母亲从未放弃过他。从被欺凌的童年到大学橄榄球明星，从越战英雄到乒乓球国手，从捕虾船长到亿万富翁，阿甘以他独特的视角经历了美国几十年的历史变迁，始终保持着纯真的心。",
        "poster_path": "/Cw4hIUIAmSYfK9QfaUW5igp9La.jpg",
        "backdrop_path": "/66Kn4XWhkuPkJxOJyPEx4U2CUfN.jpg",
        "release_date": "1994-06-23", "vote_average": 8.8,
        "genre_ids": [35, 18, 10749],
        "runtime": 142,
        "director": "罗伯特·泽米吉斯",
        "cast": [
            {"name": "汤姆·汉克斯", "character": "阿甘", "profile_path": "/oFvZoKI6lvU03n4YoNGAll9rkas.jpg"}
        ],
        "recommendations": [
            {"id": 9, "title": "楚门的世界", "original_title": "The Truman Show",
             "overview": "全球直播的真人秀。", "poster_path": "/vuza0WqY239yBXOadKlGwJsZJFE.jpg",
             "backdrop_path": "/aCHn2TXYJfzPXQKA6r9mKPbMlUB.jpg", "release_date": "1998-06-01",
             "vote_average": 8.4, "genre_ids": [35, 18]},
            {"id": 3, "title": "肖申克的救赎", "original_title": "The Shawshank Redemption",
             "overview": "银行家的越狱传奇。", "poster_path": "/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
             "backdrop_path": "/zfbjgQE1uSd9wiPTX4VzsLi0rGG.jpg", "release_date": "1994-09-23",
             "vote_average": 9.3, "genre_ids": [18]}
        ]
    },
    13: {
        "id": 13, "title": "釜山行", "original_title": "Train to Busan",
        "overview": "一列从首尔开往釜山的高速列车上，突然爆发丧尸病毒。基金经理石宇带着女儿秀安乘坐这趟列车，在封闭的车厢中乘客们为了生存展开了殊死搏斗。在被感染的人群中，人性的光辉与黑暗在生死关头被无限放大。",
        "poster_path": "/vNVFt6dtcqnI7hqa6LFBUibuFiw.jpg",
        "backdrop_path": "/qFKb25O9ROiGYt3GwtuXG5Lb2J.jpg",
        "release_date": "2016-07-20", "vote_average": 7.6,
        "genre_ids": [27, 28, 53],
        "runtime": 118,
        "director": "延尚昊",
        "cast": [
            {"name": "孔刘", "character": "石宇", "profile_path": "/ocGoFb6TrK3uWGXt4WnuibUG1vD.jpg"},
            {"name": "马东锡", "character": "尚华", "profile_path": "/ckxoXz3l4mCcHEIRaqUc7oGoIFg.jpg"}
        ],
        "recommendations": [
            {"id": 8, "title": "这个杀手不太冷", "original_title": "Léon: The Professional",
             "overview": "职业杀手与小女孩的温情故事。", "poster_path": "/wT9bYGpoFnJGiRaRF9DErVjZ7qo.jpg",
             "backdrop_path": "/qqHQsStV6exghCM7zbObuYBiYxw.jpg", "release_date": "1994-09-14",
             "vote_average": 8.5, "genre_ids": [28, 18, 53]},
            {"id": 7, "title": "盗梦空间", "original_title": "Inception",
             "overview": "潜入梦境盗取秘密。", "poster_path": "/xlaY2zyzMfkhk0HSC5VUwzoZPU1.jpg",
             "backdrop_path": "/8ZTVqvKDQ8emSGUEMjsS4yHAwrp.jpg", "release_date": "2010-07-15",
             "vote_average": 8.8, "genre_ids": [28, 878, 12]}
        ]
    },
    14: {
        "id": 14, "title": "怦然心动", "original_title": "Flipped",
        "overview": "朱莉安娜·贝克从二年级起就对搬来的邻居男孩布莱斯一见钟情，她热情主动的追求让布莱斯避之不及。然而随着时间推移，布莱斯渐渐发现了朱莉独特的魅力。当他们终于看清彼此的心意时，成长中的怦然心动已悄然改变了两人。",
        "poster_path": "/6zDYFigohwncqFL00MKbFV01dWb.jpg",
        "backdrop_path": "/xBSwwkAYl9h8QVG2OxNpSaSgJwr.jpg",
        "release_date": "2010-07-26", "vote_average": 8.2,
        "genre_ids": [35, 10749],
        "runtime": 90,
        "director": "罗伯·莱纳",
        "cast": [
            {"name": "卡兰·麦克奥利菲", "character": "布莱斯·罗斯基", "profile_path": "/prb72bUO481G2Kxk55dD0LLnCAj.jpg"},
            {"name": "玛德琳·卡罗尔", "character": "朱莉安娜·贝克", "profile_path": "/rUXWRKgyf9vLoC4zSHlu5fHdtxR.jpg"}
        ],
        "recommendations": [
            {"id": 9, "title": "楚门的世界", "original_title": "The Truman Show",
             "overview": "全球直播的真人秀。", "poster_path": "/vuza0WqY239yBXOadKlGwJsZJFE.jpg",
             "backdrop_path": "/aCHn2TXYJfzPXQKA6r9mKPbMlUB.jpg", "release_date": "1998-06-01",
             "vote_average": 8.4, "genre_ids": [35, 18]},
            {"id": 12, "title": "阿甘正传", "original_title": "Forrest Gump",
             "overview": "一个低能儿创造的奇迹。", "poster_path": "/Cw4hIUIAmSYfK9QfaUW5igp9La.jpg",
             "backdrop_path": "/66Kn4XWhkuPkJxOJyPEx4U2CUfN.jpg", "release_date": "1994-06-23",
             "vote_average": 8.8, "genre_ids": [35, 18, 10749]}
        ]
    },
    15: {
        "id": 15, "title": "海上钢琴师", "original_title": "The Legend of 1900",
        "overview": "1900年，一个婴儿在远洋邮轮维吉尼亚号上被遗弃，船上的水手收养了他，取名1900。这个从未踏足陆地的孩子在钢琴上展现出绝世天赋，成为船上的钢琴师。面对外面的世界，他选择了一生与音乐和大海为伴。",
        "poster_path": "/iOcbJ5pxokOPDRgieVDbsFMrCc6.jpg",
        "backdrop_path": "/muSeX7fnNw0pv4zHK7RSwZln6Hk.jpg",
        "release_date": "1998-10-28", "vote_average": 8.6,
        "genre_ids": [18, 10402],
        "runtime": 165,
        "director": "朱塞佩·托纳多雷",
        "cast": [
            {"name": "蒂姆·罗斯", "character": "1900", "profile_path": "/qSizF2i9gz6c6DbAC5RoIq8sVqX.jpg"}
        ],
        "recommendations": [
            {"id": 18, "title": "霸王别姬", "original_title": "Farewell My Concubine",
             "overview": "横跨半世纪的悲欢离合。", "poster_path": "/f54hNIiHNINw3JiUJB2XaQl5wCN.jpg",
             "backdrop_path": "/bBiZN1epQTu3F8iFLBuMhc4TRzr.jpg", "release_date": "1993-01-01",
             "vote_average": 9.6, "genre_ids": [18, 10749, 36]},
            {"id": 3, "title": "肖申克的救赎", "original_title": "The Shawshank Redemption",
             "overview": "银行家的越狱传奇。", "poster_path": "/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
             "backdrop_path": "/zfbjgQE1uSd9wiPTX4VzsLi0rGG.jpg", "release_date": "1994-09-23",
             "vote_average": 9.3, "genre_ids": [18]}
        ]
    },
    16: {
        "id": 16, "title": "唐探1900", "original_title": "Detective Chinatown 1900",
        "overview": "1900年的美国旧金山，唐人街发生了一起离奇的密室谋杀案。华人留学生和当地华人侦探联手展开调查，在种族歧视与排华浪潮的背景下，他们必须赶在真凶再次作案之前解开谜团。",
        "poster_path": "/g3GsgIlH3fA4RxhNOAMvSbVWyfW.jpg",
        "backdrop_path": "/4xN3phAX024b251CPhy8zvsXbBc.jpg",
        "release_date": "2025-01-29", "vote_average": 7.0,
        "genre_ids": [35, 9648, 80],
        "runtime": 136,
        "director": "陈思诚",
        "cast": [
            {"name": "王宝强", "character": "唐仁", "profile_path": "/sI74unTQvKFYb92MaPcQ4lympry.jpg"},
            {"name": "刘昊然", "character": "秦风", "profile_path": "/w600_and_h900_face/3m6zJtGo0oQSxvmUOn0urhEY7fg.jpg"}
        ],
        "recommendations": [
            {"id": 6, "title": "让子弹飞", "original_title": "Let the Bullets Fly",
             "overview": "土匪与恶霸的智斗。", "poster_path": "/pkwBO3XkQLhgb31vl5ZwmGC5meT.jpg",
             "backdrop_path": "/k1ziDzX0u8HgrAYshMb082nvtrF.jpg", "release_date": "2010-12-16",
             "vote_average": 8.8, "genre_ids": [28, 35, 80]},
            {"id": 8, "title": "这个杀手不太冷", "original_title": "Léon: The Professional",
             "overview": "职业杀手与小女孩的温情故事。", "poster_path": "/wT9bYGpoFnJGiRaRF9DErVjZ7qo.jpg",
             "backdrop_path": "/qqHQsStV6exghCM7zbObuYBiYxw.jpg", "release_date": "1994-09-14",
             "vote_average": 8.5, "genre_ids": [28, 18, 53]}
        ]
    },
    17: {
        "id": 17, "title": "寻梦环游记", "original_title": "Coco",
        "overview": "热爱音乐的小男孩米格生活在一个禁止音乐的家庭中，在亡灵节那天，他意外穿越到了亡灵世界。在那里他遇到了已故的曾曾祖父，两人踏上了寻找音乐梦想的旅程。米格逐渐理解了家族与梦想之间的真正意义。",
        "poster_path": "/6Ryitt95xrO8KXuqRGm1fUuNwqF.jpg",
        "backdrop_path": "/g7CHF8gTLGooTbP4GznIGwaqAGL.jpg",
        "release_date": "2017-10-27", "vote_average": 8.4,
        "genre_ids": [16, 14, 10751],
        "runtime": 105,
        "director": "李·昂克里奇",
        "cast": [
            {"name": "安东尼·冈萨雷斯", "character": "米格（配音）", "profile_path": "/WF7bn6t0LkxwBWyDMWvomVujn7.jpg"},
            {"name": "盖尔·加西亚·贝纳尔", "character": "埃克托（配音）", "profile_path": "/7uEO29wtdyY9bjt2JN43gVpE6vt.jpg"}
        ],
        "recommendations": [
            {"id": 10, "title": "疯狂动物城", "original_title": "Zootopia",
             "overview": "动物都市的警察梦。", "poster_path": "/hlK0e0wAQ3VLuJcsfIYPvb4JVud.jpg",
             "backdrop_path": "/9tOkjBEiiGcaClgJFtwocStZvIT.jpg", "release_date": "2016-02-11",
             "vote_average": 8.0, "genre_ids": [16, 35, 10751]},
            {"id": 4, "title": "千与千寻", "original_title": "Spirited Away",
             "overview": "少女在神灵世界的奇幻冒险。", "poster_path": "/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
             "backdrop_path": "/dyJvKsNs2KP8qQnAXbRwDjblViy.jpg", "release_date": "2001-07-20",
             "vote_average": 8.6, "genre_ids": [16, 14, 10751]}
        ]
    },
    18: {
        "id": 18, "title": "霸王别姬", "original_title": "Farewell My Concubine",
        "overview": "段小楼与程蝶衣从小在戏班学艺，两人合演《霸王别姬》誉满京城。然而在半个世纪的时代变迁中，他们的命运随着历史的风浪起伏。蝶衣对师兄小楼的执着情感、小楼的现实选择，以及菊仙的出现，最终酿成了一出动人的悲剧。",
        "poster_path": "/f54hNIiHNINw3JiUJB2XaQl5wCN.jpg",
        "backdrop_path": "/bBiZN1epQTu3F8iFLBuMhc4TRzr.jpg",
        "release_date": "1993-01-01", "vote_average": 9.6,
        "genre_ids": [18, 10749, 36],
        "runtime": 171,
        "director": "陈凯歌",
        "cast": [
            {"name": "张国荣", "character": "程蝶衣", "profile_path": "/xdSUevukGCrayOdLd4Kd6YSJnKR.jpg"},
            {"name": "张丰毅", "character": "段小楼", "profile_path": "/w600_and_h900_face/l3PtQzEU84l7B9XA6SitAGIIJqH.jpg"},
            {"name": "巩俐", "character": "菊仙", "profile_path": "/m3q1rIEdZmOnUVC0MSo1FcIGvp9.jpg"}
        ],
        "recommendations": [
            {"id": 15, "title": "海上钢琴师", "original_title": "The Legend of 1900",
             "overview": "邮轮上的钢琴天才。", "poster_path": "/iOcbJ5pxokOPDRgieVDbsFMrCc6.jpg",
             "backdrop_path": "/muSeX7fnNw0pv4zHK7RSwZln6Hk.jpg", "release_date": "1998-10-28",
             "vote_average": 8.6, "genre_ids": [18, 10402]},
            {"id": 3, "title": "肖申克的救赎", "original_title": "The Shawshank Redemption",
             "overview": "银行家的越狱传奇。", "poster_path": "/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
             "backdrop_path": "/zfbjgQE1uSd9wiPTX4VzsLi0rGG.jpg", "release_date": "1994-09-23",
             "vote_average": 9.3, "genre_ids": [18]}
        ]
    },
    19: {
        "id": 19, "title": "泰勒·斯威夫特：时代巡回演唱会", "original_title": "Taylor Swift: The Eras Tour",
        "overview": "泰勒·斯威夫特破纪录的时代巡回演唱会在大银幕上精彩呈现。从《Lover》到《Fearless》，从《evermore》到《Reputation》，这部演唱会电影收录了跨越她职业生涯多个音乐时代的经典曲目，为粉丝带来沉浸式的视听盛宴。",
        "poster_path": "/jf3YO8hOqGHCupsREf5qymYq1n.jpg",
        "backdrop_path": "/wVJG3u5Ru9tInxYiTCrJr4MpJ7Z.jpg",
        "release_date": "2023-10-13", "vote_average": 8.3,
        "genre_ids": [10402, 99],
        "runtime": 169,
        "director": "萨姆·伦奇",
        "cast": [
            {"name": "泰勒·斯威夫特", "character": "本人", "profile_path": "/rixYX4rVlWUhg0BWvclkFUNVYht.jpg"}
        ],
        "recommendations": [
            {"id": 15, "title": "海上钢琴师", "original_title": "The Legend of 1900",
             "overview": "邮轮上的钢琴天才。", "poster_path": "/iOcbJ5pxokOPDRgieVDbsFMrCc6.jpg",
             "backdrop_path": "/muSeX7fnNw0pv4zHK7RSwZln6Hk.jpg", "release_date": "1998-10-28",
             "vote_average": 8.6, "genre_ids": [18, 10402]},
            {"id": 10, "title": "疯狂动物城", "original_title": "Zootopia",
             "overview": "动物都市的警察梦。", "poster_path": "/hlK0e0wAQ3VLuJcsfIYPvb4JVud.jpg",
             "backdrop_path": "/9tOkjBEiiGcaClgJFtwocStZvIT.jpg", "release_date": "2016-02-11",
             "vote_average": 8.0, "genre_ids": [16, 35, 10751]}
        ]
    },
    20: {
        "id": 20, "title": "奥本海默", "original_title": "Oppenheimer",
        "overview": "讲述了美国\"原子弹之父\"罗伯特·奥本海默的故事。他在二战期间领导曼哈顿计划成功研制出原子弹，但也因此陷入了深深的道义谴责。战后他反对氢弹研发，却因此遭到政治迫害。这是一部关于天才、权力与良知的史诗。",
        "poster_path": "/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
        "backdrop_path": "/neeNHeXjMF5fXoCJRsOmkNGC7q.jpg",
        "release_date": "2023-07-19", "vote_average": 8.5,
        "genre_ids": [18, 36],
        "runtime": 180,
        "director": "克里斯托弗·诺兰",
        "cast": [
            {"name": "基里安·墨菲", "character": "罗伯特·奥本海默", "profile_path": "/2lKs67r7FI4bPu0AXxMUJZxmUXn.jpg"},
            {"name": "小罗伯特·唐尼", "character": "刘易斯·施特劳斯", "profile_path": "/5qHNjhtjMD4YWH3UP0rm4tKwxCL.jpg"}
        ],
        "recommendations": [
            {"id": 5, "title": "星际穿越", "original_title": "Interstellar",
             "overview": "穿越虫洞为人类寻找新家园。", "poster_path": "/yQvGrMoipbRoddT0ZR8tPoR7NfX.jpg",
             "backdrop_path": "/2ssWTSVklAEc98frZUQhgtGHx7s.jpg", "release_date": "2014-11-05",
             "vote_average": 8.7, "genre_ids": [878, 12, 18]},
            {"id": 3, "title": "肖申克的救赎", "original_title": "The Shawshank Redemption",
             "overview": "银行家的越狱传奇。", "poster_path": "/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
             "backdrop_path": "/zfbjgQE1uSd9wiPTX4VzsLi0rGG.jpg", "release_date": "1994-09-23",
             "vote_average": 9.3, "genre_ids": [18]}
        ]
    }
}

# 内存数据库：统一存储所有电影数据和详情，供 search / discover 的 Mock 模式查询
MOCK_DB: dict = {
    "movies": {
        1: MOVIES_POPULAR["results"][0],
        2: MOVIES_POPULAR["results"][1],
        3: MOVIES_POPULAR["results"][2],
        4: MOVIES_POPULAR["results"][3],
        5: MOVIES_POPULAR["results"][4],
        6: MOVIES_POPULAR["results"][5],
        7: MOVIES_POPULAR["results"][6],
        8: MOVIES_POPULAR["results"][7],
        9: MOVIES_POPULAR["results"][8],
        10: MOVIES_POPULAR["results"][9],
        11: MOVIES_POPULAR["results"][10],
        12: MOVIES_POPULAR["results"][11],
        13: MOVIES_POPULAR["results"][12],
        14: MOVIES_POPULAR["results"][13],
        15: MOVIES_POPULAR["results"][14],
        16: MOVIES_POPULAR["results"][15],
        17: MOVIES_POPULAR["results"][16],
        18: MOVIES_POPULAR["results"][17],
        19: MOVIES_POPULAR["results"][18],
        20: MOVIES_POPULAR["results"][19]
    },
    "details": MOVIE_DETAILS
}

# TMDB 类型 ID → 中文名称映射表
GENRE_MAP: dict = {
    28: "动作", 12: "冒险", 16: "动画", 35: "喜剧", 80: "犯罪",
    99: "纪录片", 18: "剧情", 10751: "家庭", 14: "奇幻", 36: "历史",
    27: "恐怖", 10402: "音乐", 9648: "悬疑", 10749: "爱情",
    878: "科幻", 53: "惊悚", 10752: "战争", 37: "西部"
}
