from sklearn.preprocessing import LabelEncoder


def fillna(df):
    df['Age'].fillna(df['Age'].mean,inplace=True)
    df['Cabin'].fillna('N',inplace=True)
    df['Embarked'].fillna('N',inplace=True)
    df['Fare'].fillna(0,inplace=True)
    return df

#불필요한 feature값 삭제
def drop_features(df):
    df.drop(['PassengerId','Name','Ticket'],axis=1,inplace=True)
    return df

#레이블 인코딩 수행
def format_features(df):
    df['Cabin']=df['Cabin'][:1]
    features = ['Cabin','Sex','Embarked']
    for feature in features:
        le = LabelEncoder()
        le = le.fit(df[feature])
        df[feature] = le.transform(df[feature])
    return df

#작성 함수 호출
def transform_features(df):
    df = fillna(df)
    df = drop_features(df)
    df=format_features(df)
    return df