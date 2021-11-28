package md5pipeline

type MD5Pipeline struct {
    numOfWorkers int
}

func NewPipeline(numOfWorkers int) MD5Pipeline {
    return MD5Pipeline{numOfWorkers: numOfWorkers}
}