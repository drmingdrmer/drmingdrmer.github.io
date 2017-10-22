package main
import (
	"log"
	"net"
	"runtime"
	"time"
)
func main() {
	runtime.GOMAXPROCS(2)
	l, err := net.Listen("tcp", ":2000")
	if err != nil {
		log.Fatal(err)
	}

	show_bug := false
	if show_bug {
		// TCPListener.File() calls dup() that switches the fd to blocking
		// mode
		l.(*net.TCPListener).File()
	}

	go func() {
		log.Println("listening... expect an 'closed **' error in 1 second")
		_, e := l.Accept()
		log.Println(e)
	}()
	time.Sleep(time.Second * 1)
	l.Close()
	time.Sleep(time.Second * 1)
}
