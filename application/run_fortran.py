from subprocess import check_output, CalledProcessError, PIPE
import subprocess


def compile_fortran_code(code_in):
    with open("test.f90", "w") as f:
        f.writelines(code_in)
    try:
        res = check_output(
            ["gfortran", "-o", "test.a", "test.f90"],
            stderr=subprocess.STDOUT,
            stdin=PIPE,
        )
    except CalledProcessError as pe:
        pass
        # print("BEFORE")
        # print(pe.output)
        # print(pe.args)
        # print(pe)
        # print(pe.stdout)
        # print(pe.stderr)
        # print(pe.stderr)
        # print("AFTER")


def run_fortran_code(name_in):
    pass


def clean_up_fortran_code(name_in):
    pass


if __name__ == "__main__":
    program = """program main
implict none
real(kind=8):: a
a = 10
write(*,*) a
end program main
	"""
    program_name = compile_fortran_code(program)
    results = run_fortran_code(program_name)
    clean_up_fortran_code(program_name)
