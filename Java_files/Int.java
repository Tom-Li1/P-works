public class Int {
	public static void main(String[] args) {
		int n = 100; //定义变量n并且赋值为100
		System.out.println("n = " + n); //打印n的值

		n = 200; //n赋值为200
		System.out.println("n = " + n); //打印变量n

		int x = n; // 定义变量x并复制为n
		System.out.println("x = " + x); // 打印变量x

		x = x + 100; // 为x复制为x+100
		System.out.println("x = " + x); // 打印x的值
		System.out.println("n = " + n); // 再次打印n的值
	}
}