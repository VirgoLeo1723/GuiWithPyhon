cursor.execute("INSERT INTO vocabulary VALUES (:word, :kind, :mean)",
            {
                'word': wordTemp,
                'kind': kindTemp,
                'mean': meanTemp
            }
        )